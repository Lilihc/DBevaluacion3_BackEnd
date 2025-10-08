from django.contrib import admin
# En views.py, admin.py, etc.
from .models import Alumno

# Register your models here.

admin.site.register(Alumno)