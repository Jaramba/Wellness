from django.db import models
from uhai.records.models import Record
from uhai.core.models import *

class Company(OwnerModel):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=200)
    date_edited = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.name
        
class HealthInsuranceProvider(Company):
    class Meta:
        permissions = (
            ('view_healthinsuranceprovider', 'View health insurance provider'),
        )

class EmployerCompany(Company):
    contact_person_name = models.CharField(max_length=100, null=True)
    insurance_providers = models.ManyToManyField('HealthInsuranceProvider')    
    
    class Meta:
        verbose_name_plural = 'Employer companies'
        permissions = (
            ('view_employercompany', 'View Employer company'),
        )

class InsuranceType(MetaData):pass
class Insurance(OwnerModel):
    plan_id = models.CharField('Policy/Plan ID', max_length=70)
    plan_name = models.CharField(max_length=50)
    type = models.ForeignKey('InsuranceType')
    policy_provider = models.ForeignKey('HealthInsuranceProvider')
    notes = models.TextField(null=True, blank=True)
    
    class Meta:
        permissions = (
            ('view_insurance', 'View insurance'),
        )
    
    def __unicode__(self):
        return self.plan_name

class PatientInsurance(OwnerModel):
    STATUS = (
        (0, "Inactive"),
        (1, "Approved"),
        (2, "Suspended"),
        (3, "Expired")
    )
    patient = models.ForeignKey("patients.Patient")    
    coverage_start_date = models.DateField()
    coverage_end_date = models.DateField()
    insurance = models.ForeignKey('Insurance', help_text='Type of cover')
    status = models.IntegerField(choices=STATUS)
    subscriber_policy_id = models.CharField(max_length=100)
    notes = models.TextField()
    
    class Meta:
        permissions = (
            ('view_patientinsurance', 'View patient insurance'),
        )
