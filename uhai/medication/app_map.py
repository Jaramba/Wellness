from forms import *

MODULE_NAME = 'uhai.medication.views'
APP_MAP={
   'prescription':{
		'model':Prescription,
		'forms':{
			'patient': PatientPrescriptionForm,
		},
		'actions':'CRUDL',
	},
	'medication':{
		'model':Medication,
		'forms':{
			'patient': MedicationForm,
		},
		'actions':'CRUDL',
	},
	'immunization':{
		'model':Immunization,
		'forms':{
			'patient': PatientImmunizationForm,
		},
		'actions':'CRUDL',
	}
}
