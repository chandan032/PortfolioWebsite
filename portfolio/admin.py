from django.contrib import admin
from .models import Info, Project, Skill
# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Info)
