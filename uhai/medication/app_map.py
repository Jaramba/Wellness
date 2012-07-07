from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
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
