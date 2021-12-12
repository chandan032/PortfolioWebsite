from django.shortcuts import render
from .models import Info, Project, Skill

# Create your views here.


def Index(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    info = Info.objects.first()
    context = {'skills': skills,
               'projects': projects,
               'info': info}
    return render(request, 'index.html', context)
