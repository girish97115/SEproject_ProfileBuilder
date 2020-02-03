from django.contrib import admin

# Register your models here.
from .models import FacultyProfile, StudentProfile ,Publication
# Register your models here.
admin.site.register(FacultyProfile)
admin.site.register(StudentProfile)
admin.site.register(Publication)