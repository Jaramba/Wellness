from django.contrib.auth.models import Group

def request(request):
    return {'user_groups': Group.objects.all()}