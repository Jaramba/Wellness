"""
This module contains the base classes for the dashboard and dashboard modules.
"""
from django.db import models

class DashboardPreferences(models.Model):
    """
    This model represents the dashboard preferences for a user.
    """
    user = models.ForeignKey('auth.User')
    data = models.TextField()

    def __unicode__(self):
        return "%s dashboard preferences" % self.user.username

    class Meta:
        db_table = 'admin_tools_dashboard_preferences'
        ordering = ('user',)

# warnings for deprecated imports
from admin_tools.deprecate_utils import import_path_is_changed
from admin_tools.dashboard import dashboards
from admin_tools.dashboard import modules

class Dashboard(
          import_path_is_changed(
              'admin_tools.dashboard.models.Dashboard',
              'admin_tools.dashboard.Dashboard'
          ),
          dashboards.Dashboard
      ): pass
