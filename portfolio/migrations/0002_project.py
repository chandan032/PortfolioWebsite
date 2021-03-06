# Generated by Django 3.0.8 on 2021-09-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('tools', models.CharField(max_length=200)),
                ('demo', models.URLField()),
                ('github', models.URLField()),
                ('show_in_slider', models.BooleanField(default=False)),
            ],
        ),
    ]
