from django.dispatch import Signal

questionnaire_invalid = Signal(providing_args=["questionnaire"])
questionnaire_valid = Signal(providing_args=["questionnaire", "entry"])
