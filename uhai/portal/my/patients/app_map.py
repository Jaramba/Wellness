from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
   'patient':{
		'model':Patient,
		'forms':{
			'patient': PatientForm,
		},
        'view':'patient',
		'actions':'CRUDL',
	},
	'dependent':{
		'model':Relationship,
		'forms':{
		},
        'view':'relationship',
		'actions':'RL',
	}
}
