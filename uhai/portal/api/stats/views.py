from django.http import HttpResponse, Http404

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response

from django.template.context import RequestContext

def patient_delta(request):
    data = '''
        [{
            "data": [
                {"y": 0, "x": 1335744000}, 
                {"y": 0, "x": 1336348800}, 
                {"y": 0, "x": 1336953600}, 
                {"y": 0, "x": 1337558400}
                ], 
            "name": "Other"
        }, 
        {
            "data": [
                {"y": 0, "x": 1335744000}, 
                {"y": 0, "x": 1336348800}, 
                {"y": 0, "x": 1336953600}, 
                {"y": 0, "x": 1337558400}
            ], 
            "name": "0"
        }, {"data": [{"y": 0, "x": 1335744000}, {"y": 0, "x": 1336348800}, {"y": 0, "x": 1336953600}, {"y": 0, "x": 1337558400}], "name": "0.1.0"}, {"data": [{"y": 0, "x": 1335744000}, {"y": 0, "x": 1336348800}, {"y": 0, "x": 1336953600}, {"y": 0, "x": 1337558400}], "name": "0.1.1"}, {"data": [{"y": 1, "x": 1335744000}, {"y": 1, "x": 1336348800}, {"y": 5, "x": 1336953600}, {"y": 2, "x": 1337558400}], "name": "0.1.2"}, {"data": [{"y": 4, "x": 1335744000}, {"y": 5, "x": 1336348800}, {"y": 29, "x": 1336953600}, {"y": 2, "x": 1337558400}], "name": "0.1.3"}, {"data": [{"y": 0, "x": 1335744000}, {"y": 0, "x": 1336348800}, {"y": 0, "x": 1336953600}, {"y": 0, "x": 1337558400}], "name": "0.1.4"}, {"data": [{"y": 0, "x": 1335744000}, {"y": 0, "x": 1336348800}, {"y": 0, "x": 1336953600}, {"y": 0, "x": 1337558400}], "name": "0.2.0"}]
    '''
    
    return HttpResponse(data, mimetype="application/json")

@login_required
def index(request, problem_type='', data = {}, template_name="stats/index.html", *args, **kwargs):    
    return render_to_response(template_name, data, context_instance= RequestContext(request))