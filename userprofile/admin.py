from django.contrib import admin
from core.models import UserProfile
from healthprovider.models import HealthWorker
from patient.models import Patient
from core.utils import perform_raw_sql
from datetime import datetime

def get_random_string(allowed_chars='ABCDEFGHIJKLMNPQRSTUVWXYZ123456789', length=8):
	from random import choice
    return ''.join([choice(allowed_chars) for i in range(length)])

class UserProfileAdmin(admin.ModelAdmin):
	model = UserProfile

	def make_healthworker(self, request, queryset):
		for profile in queryset:
			try:
				profile.healthworker
			except HealthWorker.DoesNotExist:
				perform_raw_sql("INSERT INTO healthprovider_healthworker (userprofile_ptr_id) VALUES (%s)", [profile.id])

	make_healthworker.short_description = 'Prepare Health worker profile'

	def make_patient(self, request, queryset):
		for profile in queryset:
			try:
				profile.patient
			except Patient.DoesNotExist:
				perform_raw_sql(
					"INSERT INTO patient_patient (userprofile_ptr_id, patient_number) VALUES (%s, %s)", 
					[profile.id, 'PAT-%s-%s' % 
					(datetime.now().strftime('%Y'), get_random_string(4))]
				)
								
	make_patient.short_description = 'Prepare Patient profile'

	actions = ['make_patient', 'make_healthworker']

	list_display = [f.name for f in UserProfile._meta.fields if f.name not in (
		'user','id','phone','postal_address', 
		'province', 'country', 'latitude', 'longitude',
		'work_phone', 'home_phone', 'photo',
		'person_ptr', 'national_id'
	)]
	list_filter = ['county','province','national_id']
	list_per_page = 25
	ordering = ('date_created',)
	search_fields = list_display

admin.site.register(UserProfile, UserProfileAdmin)