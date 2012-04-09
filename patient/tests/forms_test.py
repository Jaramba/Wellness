from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from guardian.forms import BaseObjectPermissionsForm


class BaseObjectPermissionsFormTests(TestCase):
    fixtures = 'test.json'
     
    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.user = User.objects.get(pk=2)
        self.user = User.objects.get(pk=3)
        self.user = User.objects.get(pk=4)
        self.user = User.objects.get(pk=5)

    def test_not_implemented(self):
        form = MyUserObjectPermissionsForm(self.user, self.obj, {})
        self.assertRaises(NotImplementedError, form.save_obj_perms)

        field_name = form.get_obj_perms_field_name()
        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.cleaned_data[field_name]), 0)

