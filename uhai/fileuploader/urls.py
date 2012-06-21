from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('fileuploader.views',
    url(r'^$', 'upload', name="uploader"),
    url(r'^profile-pic/$', 'upload', {'directory_name':"profilepics/"}, name="profile-pic-uploader"),
    url(r'^logo/$', 'upload', {'directory_name':"logos/"}, name="logo-uploader"),
    url(r'^cv/$', 'upload', {'sizeLimit':(1024*1000*15), 'directory_name':"cvs/", 'allowedExtensions':[".docx",".doc",".pdf",".odt",".rtf"]}, name="cv-uploader"),
)
