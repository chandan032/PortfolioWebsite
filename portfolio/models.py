from django.db import models
import re
import os
from django.conf import settings


class Skill(models.Model):
    sno = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=50, verbose_name="Skill Name")
    percent = models.CharField(verbose_name="Percent", max_length=4)

    def __str__(self):
        return self.skill_name + " - " + self.percent


class Info(models.Model):
    name = models.CharField(max_length=50, verbose_name="Names")
    email = models.EmailField(max_length=50, verbose_name="Email")
    phone = models.CharField(max_length=10, verbose_name="Phone")
    linkedin = models.URLField(max_length=100, verbose_name="Linkedin")
    github = models.URLField(max_length=100, verbose_name="Github")
    resume = models.FileField(verbose_name="Resume")

    def __str__(self):
        return self.name

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)


class Project(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)
    tools = models.CharField(max_length=200, blank=False, null=False)
    demo = models.URLField()
    github = models.URLField()
    show_in_slider = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)

    def save(self, *args, **kwargs):
        self.slug = self.slug_generate()
        super(Project, self).save(*args, **kwargs)

    def slug_generate(self):
        slug = self.title.strip()
        slug = re.sub(" ", "_", slug)
        return slug.lower()
