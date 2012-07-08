from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
   'prescription':{
		'model':Prescription,
		'forms':{
			'patient': PatientPrescriptionForm,
			'health-worker': PrescriptionForm,
		},
		'actions':'CRUDL',
	},
	'medication':{
		'model':Medication,
		'forms':{
			'health-worker': MedicationForm,
		},
		'actions':'CRUDL',
	},
	'immunization':{
		'model':Immunization,
		'forms':{
			'patient': PatientImmunizationForm,
			'health-worker': ImmunizationForm,
		},
		'actions':'CRUDL',
	}
}
