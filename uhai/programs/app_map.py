from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
   'program':{
		'model':Program,
		'forms':{
			'patient': ProgramForm,
		},
		'actions':'CRUDL',
	},
	'enrolledprogram':{
		'model':EnrolledProgram,
		'forms':{
			'patient': EnrolledProgramForm,
		},
		'actions':'CRUDL',
	},
	'questionnaire':{
		'model':Questionnaire,		
		'actions':'RL',
	},
	'questionnaireresponseentry':{
		'model':QuestionnaireResponseEntry,		
		'actions':'RL',
	}
}
