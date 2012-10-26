from django.db import models
from uhai.core.models import OwnerModel, MetaData
from django.shortcuts import get_object_or_404
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
        
class HealthInsuranceProvider(models.Model):
    '''
    The Insurance providers that are enrolled into Uhai
    A company can have more than one covers
    '''
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=200)
    date_edited = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    site = models.OneToOneField("sites.Site", related_name="insuranceprovider")
    
    class Meta:
        verbose_name_plural = "Health Insurance Provider"
        
    def __unicode__(self):
        return self.name

class EmployerCompany(Company):
    '''
    The Company that is registered by the Insurance company 
    that owns the current site
    '''
    contact_person_name = models.CharField(max_length=100, null=True)
    insurance_providers = models.ManyToManyField('HealthInsuranceProvider')    
    
    class Meta:
        verbose_name_plural = "Schemes"
        verbose_name = "Scheme"

def insurance_site_callback(request, scheme_slug=None):
    request.current_insurance = get_object_or_404(HealthInsuranceProvider, slug=scheme_slug)

class InsuranceType(MetaData):pass
class Insurance(OwnerModel):
    """
    A policy for a patient to be enrolled in.
    """
    plan_id = models.CharField('Policy/Plan ID', max_length=70)
    plan_name = models.CharField(max_length=50)
    type = models.ForeignKey('InsuranceType')
    policy_provider = models.ForeignKey('HealthInsuranceProvider', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Insurance Policies"
        verbose_name = "Insurance Policy"
        permissions = (
            ('view_insurance', 'View insurance'),
        )
    
    def __unicode__(self):
        return self.plan_name
        
    def save(self, request=None, *args, **kwargs):
        if request and request.site:
            if not self.pk or not self.policy_provider:
                self.policy_provider = request.site.insuranceprovider.get()
        
        super(Insurance, self).save(request=request, *args, **kwargs)

class PatientInsurance(OwnerModel):
    """
    A juction model that highlights a Patient's many Insurance cover
    """
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
