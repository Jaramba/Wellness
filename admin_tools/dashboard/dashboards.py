"""
Module where admin tools dashboard classes are defined.
"""

from django.template.defaultfilters import slugify
from django.utils.importlib import import_module
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from admin_tools.dashboard import modules
from admin_tools.utils import get_admin_site_name


class Dashboard(object):
    """
    Base class for dashboards.
    The Dashboard class is a simple python list that has three additional
    properties:

    ``title``
        The dashboard title, by default, it is displayed above the dashboard
        in a ``h2`` tag. Default value: 'Dashboard'.

    ``template``
        The template to use to render the dashboard.
        Default value: 'admin_tools/dashboard/dashboard.html'

    ``columns``
        An integer that represents the number of columns for the dashboard.
        Default value: 2.

    If you want to customize the look of your dashboard and it's modules, you
    can declare css stylesheets and/or javascript files to include when
    rendering the dashboard (these files should be placed in your
    media path), for example::

        from admin_tools.dashboard import Dashboard

        class MyDashboard(Dashboard):
            class Media:
                css = ('css/mydashboard.css',)
                js = ('js/mydashboard.js',)

    Here's an example of a custom dashboard::

        from django.core.urlresolvers import reverse
        from django.utils.translation import ugettext_lazy as _
        from admin_tools.dashboard import modules, Dashboard

        class MyDashboard(Dashboard):

            # we want a 3 columns layout
            columns = 3

            def __init__(self, **kwargs):

                # append an app list module for "Applications"
                self.children.append(modules.AppList(
                    title=_('Applications'),
                    exclude=('django.contrib.*',),
                ))

                # append an app list module for "Administration"
                self.children.append(modules.AppList(
                    title=_('Administration'),
                    models=('django.contrib.*',),
                ))

                # append a recent actions module
                self.children.append(modules.RecentActions(
                    title=_('Recent Actions'),
                    limit=5
                ))

    Below is a screenshot of the resulting dashboard:

    .. image:: images/dashboard_example.png
    """

    title = _('Dashboard')
    template = 'admin_tools/dashboard/dashboard.html'
    columns = 2
    children = None

    class Media:
        css = ()
        js  = ()

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])
        self.children = self.children or []

    def init_with_context(self, context):
        """
        Sometimes you may need to access context or request variables to build
        your dashboard, this is what the ``init_with_context()`` method is for.
        This method is called just before the display with a
        ``django.template.RequestContext`` as unique argument, so you can
        access to all context variables and to the ``django.http.HttpRequest``.
        """
        pass

    def get_id(self):
        """
        Internal method used to distinguish different dashboards in js code.
        """
        return 'dashboard'

def dashboard_view(request, dashboard):
    if request.method == 'GET':
        dashboard.Media.js.append('js/stats/patients/admin/new.js')
        dashboard.children.append(modules.DashboardModule(
            template='admin/dashboard/modules/patients_graph.html',
            enabled=True,
            is_empty=False,
            title='Graph'
        ))

class DefaultIndexDashboard(Dashboard):    
    def init_with_context(self, context):
        request = context['request']
        dashboard_view(request, self)
 
    class Media:
        css  = ['css/rickshaw.min.css',]
        js   = ['js/rickshaw.min.js',]

class AppIndexDashboard(DefaultIndexDashboard):pass
class DefaultAppIndexDashboard(DefaultIndexDashboard):pass