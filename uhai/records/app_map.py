from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
	'diagnosis':{
		'model':Diagnosis,
		'forms':{
			'patient': DiagnosisForm,
		},
		'actions':'CRUDL',
	},
	'problemtest':{
		'model':ProblemTest,
		'forms':{
			'patient': ProblemTestForm,
		},
		'actions':'CRUDL',
	},
	'encountertestresult':{
		'model':EncounterTestResult,
		'forms':{
			'patient': EncounterTestResultForm,
		},
		'actions':'CRUDL',
	},
	'encountertest':{
		'model':EncounterTest,
		'forms':{
			'patient': EncounterTestForm,
		},
		'actions':'CRUDL',
	},
   'encounter':{
		'model':Encounter,
		'forms':{
			'patient': PatientEncounterForm,
			'health-worker': EncounterForm,
		},
		'actions':'CRUDL',
	},
	'trackingfield':{
		'model':TrackingField,
		'forms':{
			'patient': TrackingFieldForm,
		},
		'actions':'CRUDL',
	}, 
	'order':{
		'model':Order,
		'forms':{
			'patient': OrderForm,
		},
		'actions':'CRUDL',
	}, 
}