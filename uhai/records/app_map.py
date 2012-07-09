from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
	'diagnosis':{
		'model':Diagnosis,
		'forms':{
			'health-worker': DiagnosisForm,
		},
		'actions':'CRUDL',
	},
	'problemtest':{
		'model':ProblemTest,
		'forms':{
			'health-worker': ProblemTestForm,
		},
		'actions':'CRUDL',
	},
	'encountertestresult':{
		'model':EncounterTestResult,
		'forms':{
			'health-worker': EncounterTestResultForm,
		},
		'actions':'CRUDL',
	},
	'encountertest':{
		'model':EncounterTest,
		'forms':{
			'health-worker': EncounterTestForm,
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
			'health-worker': OrderForm,
		},
		'actions':'CRUDL',
	}, 
}