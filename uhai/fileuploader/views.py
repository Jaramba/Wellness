from django.shortcuts import render_to_response, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from fileuploader import qqFileUploader
from django.conf import settings
from django.template.context import RequestContext
from django.views.decorators.http import require_POST

@csrf_exempt
def upload(request, directory_name="images/", sizeLimit=(1024 * 1000 * 1),
    allowedExtensions=[".jpg", ".jpeg", ".JPEG", ".JPG"], file_format="uploads/%(username)s/%(directory_name)s"):
    if request.method == "GET":
        data = {}
        return render_to_response("demo.htm", data, context_instance=RequestContext(request))
    elif request.method == "POST":
        uploader = qqFileUploader(allowedExtensions=allowedExtensions, sizeLimit=sizeLimit)#1MB
        return HttpResponse(uploader.handleUpload(
            request, upload_directory=(file_format % {
                "username" : request.user.username,
                "directory_name" : directory_name
            }))
        )
    