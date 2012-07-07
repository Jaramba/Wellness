from forms import *

MODULE_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
   'healthcarefacility':{
		'model':HealthCareFacility,
		'forms':{
			'patient': HealthCareFacilityForm,
		},
		'actions':'CRUDL',
	},
	'healthworker':{
		'model':HealthWorker,
		'forms':{
			'patient': HealthWorkerForm,
		},
		'actions':'CRUDL',
	}, 
	'speciality':{
		'model':Speciality,
		'forms':{
			'patient': SpecialityForm,
		},
		'actions':'CRUDL',
	}, 
}
