# Register your models here.
from django.contrib import admin
from .models import Empresa
from apps.funcionarios.models import Funcionario

admin.site.register(Empresa)
