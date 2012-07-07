from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
   'patient':{
		'model':Patient,
		'forms':{
			'patient': PatientForm,
		},
		'actions':'CRUDL',
	},
	'patientemergencycontact':{
		'model':PatientEmergencyContact,
		'forms':{
			'patient': PatientEmergencyContactForm,
		},
		'actions':'CRUDL',
	}
}