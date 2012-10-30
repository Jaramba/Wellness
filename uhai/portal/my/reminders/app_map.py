from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
	'event':{
		'model':Event,
		'forms':{
			'patient': EventForm,
		},
		'actions':'CRUDL',
	}, 
}
