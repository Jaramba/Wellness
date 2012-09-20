from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext, ugettext_lazy as _

import fields
from utils import now, slugify, unique_slug

from uhai.core.models import OwnerModel, MetaData
    
class Program(OwnerModel):
    '''
    This represents either an Employee Assistance Program (EAP)
    or a Patient Assistance Program (PAP). An example is a program
    to help Alcoholics.
    '''
    name = models.CharField(max_length=100)
    problems = models.ManyToManyField("records.Problem")
    concept_notes = models.TextField(null=True, blank=True)
    expected_outcome_notes = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return str(self.name)
        
    @models.permalink
    def get_absolute_url(self):
        return ("program-detail", (self.pk,))

    class Meta:
        permissions = (
            ('view_program', 'View program'), 
        )
    
class EnrolledProgram(OwnerModel):
    '''
    Patient/Employee can be enrolled in a Program to help them
    Anyone can be enrolled to this... Even Doctors or even employees
    of Insurance companies
    Even Patients can enroll themselves to a program, for example,
    Weight loss program...
    '''
    program = models.ForeignKey("Program")
    enrollee = models.ForeignKey("patients.Patient", related_name='enrollee')
    enroller = models.ForeignKey("auth.User", related_name='enroller', verbose_name="Enrolled By")
    date_enrolled = models.DateField(auto_now=True)
    date_completed = models.DateField()
    outcome_notes = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return 'Program enrolled to: %s by %s' % (self.program, self.enrollee)
    
    class Meta:
        permissions = ( 
            ('view_enrolledprogram', 'View enrolled program'), 
        )

class ProgramWorkflow(OwnerModel):
    '''
    A program may involve certain steps that define progress
    in the program; thus we have the path and the nodes.
    The nodes are represented by the @see: ProgramWorkflowState
    and the Path represented by @see: ProgramWorkflow
    Example: An Alcoholic Program would have Workflows like:
    Family Intervention, Withdrawal...    
    '''
    name = models.CharField(max_length=100)
    program = models.ForeignKey("Program")
    concept_notes = models.TextField()
    continued = models.BooleanField(default=True)
    days = models.IntegerField(default=0, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        permissions = ( 
            ('view_enrolledprogram', 'View enrolled program'), 
        )
    
class ProgramWorkflowState(OwnerModel):
    '''
    This represents a node/milestone state of @see: PrenrolleeogramWorkflow
    in the program.
    A state in the Alcoholic Program would be: Starting, Completed, or something
    '''
    name = models.CharField(max_length=120)
    program_workflow = models.ForeignKey("ProgramWorkflow")
    weight = models.IntegerField(default=0)
    initial = models.BooleanField(default=False)
    terminal = models.BooleanField(default=False)
    concept_notes = models.TextField()
    
    def __unicode__(self):
        return 'Node: %s %s' % (self.name, self.program_workflow)
    
    class Meta:
        permissions = ( 
            ('view_programworkflowstate', 'View program workflow state'), 
        )

STATUS_DRAFT = 1
STATUS_PUBLISHED = 2
STATUS_CHOICES = (
    (STATUS_DRAFT, _("Draft")),
    (STATUS_PUBLISHED, _("Published")),
)
class QuestionnaireManager(models.Manager):
    """
    Only show published forms for non-staff users.
    """
    def published(self, for_user=None):
        if for_user is not None and for_user.is_staff:
            return self.all()
        filters = [
            Q(publish_date__lte=now()) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=now()) | Q(expiry_date__isnull=True),
            Q(status=STATUS_PUBLISHED),
        ]
        if settings.USE_SITES:
            filters.append(Q(sites=Site.objects.get_current()))
        return self.filter(*filters)

class Questionnaire(OwnerModel):
    """
    A user-built form.
    """

    sites = models.ManyToManyField(Site, editable=settings.USE_SITES,
        default=[settings.SITE_ID])
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), editable=settings.EDITABLE_SLUGS,
        max_length=100, unique=True)
    intro = models.TextField(_("Intro"), blank=True)
    button_text = models.CharField(_("Button text"), max_length=50,
        default=_("Submit"))
    response = models.TextField(_("Response"), blank=True)
    status = models.IntegerField(_("Status"), choices=STATUS_CHOICES,
        default=STATUS_PUBLISHED)
    publish_date = models.DateTimeField(_("Published from"),
        help_text=_("With published selected, won't be shown until this time"),
        blank=True, null=True)
    expiry_date = models.DateTimeField(_("Expires on"),
        help_text=_("With published selected, won't be shown after this time"),
        blank=True, null=True)
    login_required = models.BooleanField(_("Login required"),
        help_text=_("If checked, only logged in users can view the form"))
    
    objects = QuestionnaireManager()

    class Meta:
        verbose_name = _("Questionnaire")
        verbose_name_plural = _("Questionnaires")

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        """
        Create a unique slug from title - append an index and increment if it
        already exists.
        """
        if not self.slug:
            slug = slugify(self)
            self.slug = unique_slug(self.__class__.objects, "slug", slug)
        super(Questionnaire, self).save(*args, **kwargs)

    def total_entries(self):
        """
        Called by the admin list view where the queryset is annotated
        with the number of entries.
        """
        return self.total_entries
    total_entries.admin_order_field = "total_entries"

    @models.permalink
    def get_absolute_url(self):
        return ("questionnaire_detail", (), {"slug": self.slug})

    def admin_links(self):
        kw = {"args": (self.id,)}
        links = [
            (_("View questionnaire on site"), self.get_absolute_url()),
            (_("Filter entries"), reverse("admin:form_entries", **kw)),
            (_("View all entries"), reverse("admin:form_entries_show", **kw)),
            (_("Export all entries"), reverse("admin:form_entries_export", **kw)),
        ]
        for i, (text, url) in enumerate(links):
            links[i] = "<a href='%s'>%s</a>" % (url, ugettext(text))
        return "<br>".join(links)
    admin_links.allow_tags = True
    admin_links.short_description = ""

class ProgramQuestionnaire(Questionnaire):
    send_email = models.BooleanField(_("Send email"), default=True, help_text=
        _("If checked, the person entering the questionnaire will be sent an email"))
    email_from = models.EmailField(_("From address"), blank=True,
        help_text=_("The address the email will be sent from"))
    email_copies = models.CharField(_("Send copies to"), blank=True,
        help_text=_("One or more email addresses, separated by commas"),
        max_length=200)
    email_subject = models.CharField(_("Subject"), max_length=200, blank=True)
    email_message = models.TextField(_("Message"), blank=True)

    program = models.ForeignKey("Program")
    
class DiagnosisQuestionnaire(Questionnaire):pass
        
class FieldManager(models.Manager):
    """
    Only show visible fields when displaying actual form..
    """
    def visible(self):
        return self.filter(visible=True)

class Field(OwnerModel):
    """
    A field for a user-built form.
    """

    label = models.CharField(_("Label"), max_length=settings.LABEL_MAX_LENGTH)
    slug = models.SlugField(_('Slug'), max_length=100, blank=True,
            default="")
    field_type = models.IntegerField(_("Type"), choices=fields.NAMES)
    required = models.BooleanField(_("Required"), default=True)
    visible = models.BooleanField(_("Visible"), default=True)
    choices = models.CharField(_("Choices"), max_length=1000, blank=True,
        help_text="Comma separated options where applicable. If an option "
            "itself contains commas, surround the option starting with the %s"
            "character and ending with the %s character." %
                (settings.CHOICES_QUOTE, settings.CHOICES_UNQUOTE))
    default = models.CharField(_("Default value"), blank=True,
        max_length=settings.FIELD_MAX_LENGTH)
    placeholder_text = models.CharField(_("Placeholder Text"), null=True,
        blank=True, max_length=100, editable=settings.USE_HTML5)
    help_text = models.CharField(_("Help text"), blank=True, max_length=100)

    objects = FieldManager()

    questionnaire = models.ForeignKey("Questionnaire", related_name="fields")
    order = models.IntegerField(_("Order"), null=True, blank=True)
    
    def delete(self, *args, **kwargs):
        fields_after = self.questionnaire.fields.filter(order__gte=self.order)
        fields_after.update(order=models.F("order") - 1)
        super(Field, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = _("Field")
        ordering = ("order",)
        verbose_name_plural = _("Fields")

    def __unicode__(self):
        return u"%s in %s" % (self.label, self.questionnaire)

    def get_choices(self):
        """
        Parse a comma separated choice string into a list of choices taking
        into account quoted choices using the ``settings.CHOICES_QUOTE`` and
        ``settings.CHOICES_UNQUOTE`` settings.
        """
        choice = ""
        quoted = False
        
        self.choices = "Select, %s" % self.choices
        
        for char in self.choices:
            if not quoted and char == settings.CHOICES_QUOTE:
                quoted = True
            elif quoted and char == settings.CHOICES_UNQUOTE:
                quoted = False
            elif char == "," and not quoted:
                choice = choice.strip()
                if choice:
                    yield choice, choice
                choice = ""
            else:
                choice += char
                
        choice = choice.strip()
        
        if choice:
            yield choice, choice

    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = self.questionnaire.fields.count()
                
        if not self.slug:
            slug = slugify(self).replace('-', '_')
            self.slug = unique_slug(self.questionnaire.fields, "slug", slug)
        return super(Field, self).save(*args, **kwargs)

    def is_a(self, *args):
        """
        Helper that returns True if the field's type is given in any arg.
        """
        return self.field_type in args

class FieldLevel(MetaData):
    field = models.ForeignKey("Field")
    range = models.CharField(max_length=50)
        
class QuestionnaireResponseEntry(OwnerModel):
    """
    An entry submitted via a user-built form.
    """
    entry_time = models.DateTimeField(_("Date/time"))
    user = models.ForeignKey("auth.User", related_name="respondent")
    questionnaire = models.ForeignKey("Questionnaire", related_name="entries")
    
    def __unicode__(self):
        return "Response to %s by %s" % (self.questionnaire, self.user)

    class Meta:
        verbose_name = _("Questionnaire response")

class QuestionnaireFieldResponseEntry(OwnerModel):
    """
    A single field value for a questionnaire entry submitted via a user-built form.
    """

    field = models.ForeignKey("Field")
    value = models.CharField(max_length=settings.FIELD_MAX_LENGTH,
            null=True)
            
    entry = models.ForeignKey("QuestionnaireResponseEntry", related_name="fields")

    def __unicode__(self):
        return "Field Response: %s for %s" % (self.entry, self.field)

    class Meta:
        verbose_name = _("Questionnaire question response")
