from django.db.models.base import ModelBase

from django.forms.models import modelform_factory

from csv import writer
from mimetypes import guess_type
from os.path import join
from cStringIO import StringIO
from datetime import datetime

from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ungettext, ugettext_lazy as _

from uhai.utils.admin import BaseModelAdmin, BaseTabularInline

import forms
import models

from django.conf import settings
from utils import now, slugify

try:
    import xlwt
    XLWT_INSTALLED = True
    XLWT_DATETIME_STYLE = xlwt.easyxf(num_format_str='MM/DD/YYYY HH:MM:SS')
except ImportError:
    XLWT_INSTALLED = False

fs = FileSystemStorage(location=settings.UPLOAD_ROOT)
form_admin_filter_horizontal = ()

class FieldTabularInlineAdmin(BaseTabularInline):
    model = models.Field
    exclude = ('slug', )
    
class FieldLevelTabularInlineAdmin(BaseTabularInline):
    model = models.FieldLevel
    exclude = ('slug', )
    
class FieldAdmin(BaseModelAdmin):
    exclude = ('slug', )
    inlines = (FieldLevelTabularInlineAdmin,)
    search_fields = ("label", "slug", "choices", "placeholder_text")
    list_filter = ("questionnaire", "field_type")
    list_editable = ("choices",)
    list_display = ("label", "choices", "required", "visible", "default")
    list_display_links = ("label",)

class QuestionnaireAdmin(BaseModelAdmin):
    inlines = (FieldTabularInlineAdmin,)
    list_display = ("title", "status", "publish_date",
                    "expiry_date", "total_entries", "admin_links")
    list_display_links = ("title",)
    list_editable = ("status", "publish_date", "expiry_date")
    list_filter = ("status",)
    filter_horizontal = form_admin_filter_horizontal
    search_fields = ("title", "intro", "response", "email_from")
    radio_fields = {"status": admin.HORIZONTAL}
    fieldsets = form_admin_fieldsets = [
        (None, 
            {"fields": 
                ["title", "program", ("status", "login_required",),
                ("publish_date", "expiry_date",), "intro", "button_text", "response"
                ]
            }
        )
    ]

    if settings.EDITABLE_SLUGS:
        fieldsets.append(
            (_("Slug"), {"fields": ("slug",), "classes": ("collapse",)}))

    if settings.USE_SITES:
        fieldsets.append((_("Sites"), {"fields": ("sites",),
            "classes": ("collapse",)}))
    form_admin_filter_horizontal = ("sites",)


    def queryset(self, request):
        """
        Annotate the queryset with the entries count for use in the
        admin list view.
        """
        qs = super(QuestionnaireAdmin, self).queryset(request)
        return qs.annotate(total_entries=Count("entries"))

    def get_urls(self):
        """
        Add the entries view to urls.
        """
        urls = super(QuestionnaireAdmin, self).get_urls()
        extra_urls = patterns("",
            url("^(?P<form_id>\d+)/entries/$",
                self.admin_site.admin_view(self.entries_view),
                name="form_entries"),
            url("^(?P<form_id>\d+)/entries/show/$",
                self.admin_site.admin_view(self.entries_view),
                {"show": True}, name="form_entries_show"),
            url("^(?P<form_id>\d+)/entries/export/$",
                self.admin_site.admin_view(self.entries_view),
                {"export": True}, name="form_entries_export"),
            url("^file/(?P<field_entry_id>\d+)/$",
                self.admin_site.admin_view(self.file_view),
                name="form_file"),
        )
        return extra_urls + urls

    def entries_view(self, request, form_id, show=False, export=False,
                     export_xls=False):
        """
        Displays the questionnaire entries in a HTML table with option to
        export as CSV file.
        """
        if request.POST.get("back"):
            change_url = reverse("admin:%s_%s_change" %
                (Form._meta.app_label, Form.__name__.lower()), args=(form_id,))
            return HttpResponseRedirect(change_url)
        questionnaire = get_object_or_404(Form, id=form_id)
        entries_questionnaire = forms.ResponseForm(questionnaire, request, request.POST or None)
        delete_entries_perm = "%s.delete_formentry" % models.QuestionnaireResponseEntry._meta.app_label
        can_delete_entries = request.user.has_perm(delete_entries_perm)
        submitted = entries_form.is_valid() or show or export or export_xls
        export = export or request.POST.get("export")
        export_xls = export_xls or request.POST.get("export_xls")
        if submitted:
            if export:
                response = HttpResponse(mimetype="text/csv")
                fname = "%s-%s.csv" % (questionnaire.slug, slugify(now().ctime()))
                response["Content-Disposition"] = "attachment; filename=%s" % fname
                queue = StringIO()
                csv = writer(queue, delimiter=settings.CSV_DELIMITER)
                csv.writerow(entries_form.columns())
                for row in entries_form.rows(csv=True):
                    csv.writerow(row)
                # Decode and reencode entire queued response into utf-16 to be Excel compatible
                data = queue.getvalue().decode("utf-8").encode("utf-16")
                response.write(data)
                return response
            elif XLWT_INSTALLED and export_xls:
                response = HttpResponse(mimetype="application/vnd.ms-excel")
                fname = "%s-%s.xls" % (questionnaire.slug, slugify(now().ctime()))
                response["Content-Disposition"] = "attachment; filename=%s" % fname
                queue = StringIO()
                workbook = xlwt.Workbook(encoding='utf8')
                sheet = workbook.add_sheet(questionnaire.title)
                for c, col in enumerate(entries_form.columns()):
                    sheet.write(0, c, col)
                for r, row in enumerate(entries_form.rows(csv=True)):
                    for c, item in enumerate(row):
                        if isinstance(item, datetime):
                            item = item.replace(tzinfo=None)
                            sheet.write(r + 2, c, item, XLWT_DATETIME_STYLE)
                        else:
                            sheet.write(r + 2, c, item)
                workbook.save(queue)
                data = queue.getvalue()
                response.write(data)
                return response
            elif request.POST.get("delete") and can_delete_entries:
                selected = request.POST.getlist("selected")
                if selected:
                    try:
                        from django.contrib.messages import info
                    except ImportError:
                        def info(request, message, fail_silently=True):
                            request.user.message_set.create(message=message)
                    entries = models.QuestionnaireResponseEntry.objects.filter(id__in=selected)
                    count = entries.count()
                    if count > 0:
                        entries.delete()
                        message = ungettext("1 entry deleted",
                                            "%(count)s entries deleted", count)
                        info(request, message % {"count": count})
        template = "admin/forms/entries.html"
        context = {"title": _("View Entries"), "entries_form": entries_form,
                   "opts": self.model._meta, "original": questionnaire,
                   "can_delete_entries": can_delete_entries,
                   "submitted": submitted,
                   "xlwt_installed": XLWT_INSTALLED}
        return render_to_response(template, context, RequestContext(request))

    def file_view(self, request, field_entry_id):
        """
        Output the file for the requested field entry.
        """
        field_entry = get_object_or_404(QuestionnaireFieldResponseEntry, id=field_entry_id)
        path = join(fs.location, field_entry.value)
        response = HttpResponse(mimetype=guess_type(path)[0])
        f = open(path, "r+b")
        response["Content-Disposition"] = "attachment; filename=%s" % f.name
        response.write(f.read())
        f.close()
        return response

class ProgramQuestionnaireAdmin(QuestionnaireAdmin):
    fieldsets = form_admin_fieldsets = [
        (None, {"fields": ["title", "program", ("status", "login_required",),
        ("publish_date", "expiry_date",), "intro", "button_text", "response"]}),
        (_("Email"), {"fields": ("send_email", "email_from", "email_copies",
            "email_subject", "email_message")}),]
            
    list_display = ("title", "status", "email_copies", "publish_date",
                    "expiry_date", "total_entries", "admin_links")
    list_editable = ("status", "email_copies", "publish_date", "expiry_date")
    search_fields = ("title", "intro", "response", "email_from",
                     "email_copies")
    
    if settings.EDITABLE_SLUGS:
        fieldsets.append(
            (_("Slug"), {"fields": ("slug",), "classes": ("collapse",)}))

    if settings.USE_SITES:
        fieldsets.append((_("Sites"), {"fields": ("sites",),
            "classes": ("collapse",)}))
    form_admin_filter_horizontal = ("sites",)
    
class DiagnosisQuestionnaireAdmin(QuestionnaireAdmin):
    fieldsets = form_admin_fieldsets = [
        (
            None, {"fields": ["title", ("status", "login_required",),
            ("publish_date", "expiry_date",), "intro", "button_text", "response"]}
        )
    ]
    
    if settings.EDITABLE_SLUGS:
        fieldsets.append(
            (_("Slug"), {"fields": ("slug",), "classes": ("collapse",)}))

    if settings.USE_SITES:
        fieldsets.append((_("Sites"), {"fields": ("sites",),
            "classes": ("collapse",)}))
    form_admin_filter_horizontal = ("sites",)
      
admin.site.register(models.ProgramQuestionnaire, ProgramQuestionnaireAdmin)
admin.site.register(models.DiagnosisQuestionnaire, DiagnosisQuestionnaireAdmin)
admin.site.register(models.QuestionnaireResponseEntry)
admin.site.register(models.Field, FieldAdmin)
admin.site.register(models.QuestionnaireFieldResponseEntry)

class ProgramWorkflowStateInline(BaseTabularInline):
    model = models.ProgramWorkflowState
    extra = 1

class EnrolledProgramInline(BaseTabularInline):
    model = models.EnrolledProgram
    extra = 1
    
class ProgramAdmin(BaseModelAdmin):
    model = models.Program
    list_display = [f.name for f in models.Program._meta.fields if f.name not in (
        'model_owner', 'site', 'access_control_list'
    )]
    inlines = [EnrolledProgramInline]
admin.site.register(models.Program, ProgramAdmin)

class ProgramWorkflowAdmin(BaseModelAdmin):
    model = models.ProgramWorkflow
    list_display = [f.name for f in models.ProgramWorkflow._meta.fields if f.name not in (
        'model_owner', 'site', 'access_control_list'
    )]
    inlines = [ProgramWorkflowStateInline]
admin.site.register(models.ProgramWorkflow, ProgramWorkflowAdmin)

for M in [x
    for x in models.__dict__.values()  
        if (issubclass(type(x), ModelBase) and
            not x._meta.abstract and         
            x.__name__ not in [
                    'ProgramWorkflowState', 'ProgramWorkflow', 
                    'EnrolledProgram', 'Questionnaire', 'Field'
                ]
        )
]:
    class ItemAdmin(BaseModelAdmin):
        model = M     
        #form = forms.__dict__.get(M.__name__ + 'Form', 
        #        modelform_factory(M, form=forms.BaseModelForm)
        #)
        list_display = [f.name for f in M._meta.fields if not f.name in (
            'description', 'is_public','concept_notes','expected_outcome_notes',
            'model_owner', 'site', 'access_control_list'
        )]
        inlines = []
        
    try:
        admin.site.register(M, ItemAdmin)
    except admin.sites.AlreadyRegistered:
        pass
