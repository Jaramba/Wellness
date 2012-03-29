"""
@author: Ferdinand E. Silva
@email: ferdinandsilva@ferdinandsilva.com
@website: http://ferdinandsilva.com
"""
import os
from django.conf import settings
#from recruit.util import generate_code

class qqFileUploader(object):
    def __init__(self, allowedExtensions=[], sizeLimit=1024):
        self.allowedExtensions = allowedExtensions
        self.sizeLimit = sizeLimit

    def handleUpload(self, djangoRequest, storage_dir=settings.MEDIA_ROOT, upload_directory=''):
        upload_destination = (storage_dir if storage_dir.endswith('/') else storage_dir + '/') + upload_directory
        #read file info from stream
        uploaded = djangoRequest.read
        #get file size
        fileSize = int(uploaded.im_self.META["CONTENT_LENGTH"])
        #get file name
        fileName = uploaded.im_self.META["HTTP_X_FILE_NAME"]
        
        fileExtension = self._getFileExtension(fileName)
        #check first for allowed file extensions
        
        if fileExtension in self.allowedExtensions:
            #check file size
            if fileSize <= self.sizeLimit:
                #upload file
                #write file
                if not os.path.exists(upload_destination):
                    os.makedirs(upload_destination)
                
                file = open(upload_destination + fileExtension,"wb")
                file.write(djangoRequest.read(fileSize))
                file.close()
                return "{success:true, file: '%s'}" % (upload_directory + fileExtension)
            else:
                return '{"error":"File is too large."}'
        else:
            return '{"error":"File has an invalid extension."}'

    def _getFileExtension(self,fileName):
        filename, extension = os.path.splitext(fileName)
        return extension 
        
    
