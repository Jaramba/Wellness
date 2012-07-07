from forms import *

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
   'employercompany':{
		'model':EmployerCompany,
		'forms':{
			'patient': EmployerCompanyForm,
		},
		'actions':'RL',
	},
	'healthinsuranceprovider':{
		'model':HealthInsuranceProvider,
		'actions':'RL',
	},
	'insurance':{
		'model':Insurance,
		'forms':{
			'patient': InsuranceForm,
		},
		'actions':'RL',
	}, 
	'patientinsurance':{
		'model':PatientInsurance,
		'forms':{
			'patient': PatientInsuranceForm,
		},
		'actions':'CRUDL',
	}, 
}