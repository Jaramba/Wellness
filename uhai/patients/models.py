from uhai.core.models import OwnerModel, MetaData
from uhai.core.utils import pkgen
from uhai.userprofile.models import *

from django.contrib.auth.models import User
from django.db import transaction

from uhai.providers.models import HealthWorker

class Patient(OwnerModel):
    '''
    Have a model to save patient details... of cos Profile is linked to user, so, 
    we dont have to worry about it
    '''
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    DIET_TYPE=[]
    BLOOD_GROUPS = [
        ('a-positive','A+'),
        ('a-negative','A-'),
        ('b-positive','B+'),
        ('b-negative','B-'),
        ('ab-positive','AB+'),
        ('ab-negative','AB-'),
        ('o-positive','O+'),
        ('o-negative','O-'),
    ]

    user = models.ForeignKey('auth.User', unique=True)

    gender = models.CharField(max_length=20, choices=GENDER, null=True)
    date_of_birth = models.DateField(null=True, help_text='The Patient\'s indicated date of birth')

    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUPS, null=True)
    weight = models.CharField(max_length=5, default=0, null=True, help_text='Enter weight in Kilograms (Kgs)')
    height = models.CharField(max_length=7, default=0, null=True, help_text='Enter standard height, eg: 5\'9" for 5 foot 9 inch')

    employer  = models.ForeignKey('insurance.EmployerCompany', null=True)
    insurance = models.ManyToManyField('insurance.Insurance', through='insurance.PatientInsurance')
    providers = models.ManyToManyField('providers.HealthWorker', through='providers.PatientProvider')
    
    def __unicode__(self):
        return '%s' % self.user
    
    class Meta:
        permissions = ( 
            ('view_patient', 'View patient'), 
        )
        verbose_name_plural = 'Patient Profile'
        
class RelationshipType(OwnerModel):
    '''
    try and defile the relationship between a user and another
    '''
    a_is_to_b = models.CharField(max_length=50)
    b_is_to_a = models.CharField(max_length=50)
    preffered = models.BooleanField(default=False)
    dependent = models.BooleanField(default=False)
            
    def __unicode__(self):
        return self.a_is_to_b + ' - ' + self.b_is_to_a

class Relationship(OwnerModel):
    '''
    A patient can decide to add family and track their files;
    Only this patient can then decide to give access to HealthWorkers
    Even the dependants can log in, only that the access to the information 
    on the dependants is restricted after they attain 18 years.
    Registration claim
    '''
    person_a = models.ForeignKey('auth.User', verbose_name='Patient', related_name='person_a')
    person_b = models.ForeignKey('auth.User', verbose_name='Relative', related_name='person_b')
    next_of_kin = models.BooleanField(default=False)
    relationship = models.ForeignKey(RelationshipType)
    
    def __unicode__(self):
        return '%s and %s (%s)' % (self.person_a, self.person_b, self.relationship)
    
    @transaction.commit_on_success
    def save(self, *args, **kwargs):
        if self.person_a_id and self.person_b_id and (self.person_a_id == self.person_b_id):
            class CircularRelationException(Exception):pass
            raise CircularRelationException('Sorry. You cannot set yourself as a relation')
        else:
            super(Relationship, self).save(*args, **kwargs)
