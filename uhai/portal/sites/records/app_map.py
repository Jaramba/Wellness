from models import *
from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
	'diagnosis':{
		'model':Diagnosis,
		'forms':{
			'health-worker': DiagnosisForm,
		},
		'view': 'secured_role_model_view',
		'actions':'CRUDL',
	},
	'problemtest':{
		'model':ProblemTest,
		'forms':{
			'health-worker': ProblemTestForm,
		},
		'view': 'secured_role_model_view',
		'actions':'CRUDL',
	},
	'encountertestresult':{
		'model':EncounterTestResult,
		'forms':{
			'health-worker': EncounterTestResultForm,
		},
		'view': 'secured_role_model_view',
		'actions':'CRUDL',
	},
	'encountertest':{
		'model':EncounterTest,
		'forms':{
			'health-worker': EncounterTestForm,
		},
		'view': 'secured_role_model_view',
		'actions':'CRUDL',
	},
   'encounter':{
		'model':Encounter,
		'forms':{
			'patient': PatientEncounterForm,
			'health-worker': EncounterForm,
		},
		'view': 'encounter',
		'actions':'CRUDL',
	},
	'order':{
		'model':Order,
		'forms':{
			'health-worker': OrderForm,
		},
		'view': 'secured_role_model_view',
		'actions':'CRUDL',
	}, 
}