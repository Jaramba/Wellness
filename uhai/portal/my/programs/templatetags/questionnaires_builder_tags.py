from django import template
from django.template.loader import get_template

from ..forms import QuestionnaireForm
from ..models import Questionnaire

register = template.Library()

class BuiltQuestionnaireNode(template.Node):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self, context):
        request = context["request"]
        user = getattr(request, "user", None)
        post = getattr(request, "POST", None)
        files = getattr(request, "FILES", None)
        if self.name != "questionnaire":
            lookup = {
                str(self.name): template.Variable(self.value).resolve(context)
            }
            try:
                questionnaire = Questionnaire.objects.published(for_user=user).get(**lookup)
            except Questionnaire.DoesNotExist:
                questionnaire = None
        else:
            questionnaire = template.Variable(self.value).resolve(context)
        if not isinstance(questionnaire, Questionnaire) or (questionnaire.login_required and not
                                          user.is_authenticated()):
            return ""
        t = get_template("questionnaires/includes/built_form.html")
        context["questionnaire"] = questionnaire
        return t.render(context)

@register.tag
def render_built_questionnaire(parser, token):
    """
    render_build_questionnaire takes one argument in one of the following formats:

    {% render_build_questionnaire form_instance %}
    {% render_build_questionnaire form=form_instance %}
    {% render_build_questionnaire id=form_instance.id %}
    {% render_build_questionnaire slug=form_instance.slug %}

    """
    try:
        _, arg = token.split_contents()
        if "=" not in arg:
            arg = "questionnaire=" + arg
        name, value = arg.split("=", 1)
        if name not in ("form", "questionnaire", "id", "slug"):
            raise ValueError
    except ValueError:
		e = ()
		raise template.TemplateSyntaxError(render_built_questionnaire.__doc__)
    return BuiltQuestionnaireNode(name, value)
