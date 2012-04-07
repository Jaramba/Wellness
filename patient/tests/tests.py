from django.test import TestCase
from django.contrib.auth.models import User

class BaseTestCase(TestCase):
    def setUp(self):
        self.users = [
            User.objects.get(pk=1),
            User.objects.get(pk=2),
            User.objects.get(pk=3),
            User.objects.get(pk=4)
        ]
        
    def _sort_by_pk(self, list_or_qs):
        annotated = [(item.pk, item) for item in list_or_qs]
        annotated.sort()
        return map(lambda item_tuple: item_tuple[1], annotated)
    
    def assertQuerysetEqual(self, a, b):
        return self.assertEqual(self._sort_by_pk(a), self._sort_by_pk(b))


class PatientModelTestCase(BaseTestCase):
    
        
