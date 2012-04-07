from django.db import models
from core.models import *

from insuranceprovider.models import *

class HealthCareFacility(EmployerCompany):
	TYPES = (
		('other', 'Other'),
		('clinics', 'Clinics'),
		('Complementary', (
				('acupuncturists','Acupuncturists'), 
				('chiropractors','Chiropractors'),
				('naturopathic-medicine','Naturopathic medicine'), 
				('osteopathic', 'Osteopathic'),
				('speciality-alternative', 'speciality alternative')
			)
		),
		('Dentistry', (
				('general', 'General'),
			 	('cosmetic', 'Cosmetic'), 
			 	('dentist-referral-services', 'Dentist referral services'), 
			 	('Endodontics', 'endodontics'), 
			 	('orthodontics', 'orthodontics'), 
			 	('pediatric', 'Pediatric'), 
			 	('periodontics', 'Periodontics'), 
			 	('prosthodontics', 'Prosthodontics'), 
			 	('speciality-dental-care', 'Speciality dental care')
			 )
		),
		('Doctors',(
				('other-doctors', 'Other'),
				('allergists-immunologists', 'Allergists and Immunologists'),
				('bariatrics-doctors', 'Bariatrics Doctors'),
				('cardiologists', 'Cardiologists'),
				('dermatologists', 'Dermatologists'),
				('endocrinologists', 'Endocrinologists'),
				('ent-doctors', 'ENT Doctors'),
				('gastroenterologists', 'Gastroenterologists'),
				('general-practitioners', 'General Practitioners'), 
				('general-surgeons', 'General Surgeons'),
				('geriatrics-doctors', 'Geriatrics Doctors'),
				('gynecologists-obstetricians', 'Gynecologists and Obstetricians'),
				('internists', 'Internists'),
				('neurologists', 'Neurologists'),
				('oncologists', 'Oncologists'),
				('ophthalmologists', 'Ophthalmologists'),
				('oral-maxillofacial-surgeons', 'Oral and Maxillofacial Surgeons'),
				('orthopedists', 'Orthopedists'),
				('pediatricians', 'Pediatricians'),
				('physician-referral-services', 'Physician Referral Services'),
				('plastic-reconstructive-surgeons', 'Plastic and Reconstructive Surgeons'),
				('podiatrists', 'Podiatrists'),
				('psychiatrists', 'Psychiatrists'),
				('radiologists', 'Radiologists'),
				('urologists', 'Urologists'),
				('vascular-surgeons', 'Vascular Surgeons'),
			),
		),
		('Health care centers',(
				('assisted-living', 'Assisted Living'),
				('donor-centers', 'Donor Centers'),
				('health-care-clinics', 'Health Care Clinics'),
				('hospitals', 'Hospitals'),
				('nursing homes', 'Nursing Homes'),
				('pharmacies', 'Pharmacies')
			),
		),
		('Health care services',(
				('diagnostic-services', 'Diagnostic Services'),
				('health-associations', 'Health Associations'),
				('health-care-referral-services', 'Health Care Referral Services'),
				('home-health-care', 'Home Health Care'),
				('medical-support-services', 'Medical Support Services')
			),
		),
		('Speciality health care',(
				('other-speciality', 'Other'),
				('addiction', 'Addiction'),
				('cancer-services', 'Cancer Services'),
				('counseling', 'Counseling'),
				('dialysis', 'Dialysis'),
				('hospice', 'Hospice'),
				('laser-vision-correction', 'Laser Vision Correction'),
				('mens-health', 'Men\'s Health'),
				('hospice', 'Hospice'),
				('mental-health', 'Mental Health Services'),
				('nutrition', 'Nutrition'),
				('optometrists', 'Optometrists'),
				('pain-management', 'Pain Management'),
				('physical-therapy', 'Physical Therapy'),
				('sleep-disorders', 'Sleep Disorders'),
				('speech-hearing', 'Speech and Hearing'),
				('sports-medicine', 'Sports Medicine'),
				('weight-loss', 'Weight Loss'),
				('womens-health', 'Women\'s Health'), 
			),
		),
	)
	speciality = models.CharField(max_length=50, choices=TYPES)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Health care facilities'

class HealthWorker(models.Model):
	profile = models.ForeignKey(UserProfile)
	speciality = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.profile.full_name
