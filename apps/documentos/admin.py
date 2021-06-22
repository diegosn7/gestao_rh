from django.contrib import admin
#from .models import Documento
from apps.documentos.models import Documento
# Register your models here.
admin.site.register(Documento)