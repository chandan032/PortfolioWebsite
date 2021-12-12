# Generated by Django 3.0.8 on 2021-08-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=50, verbose_name='Skill Name')),
                ('percent', models.CharField(max_length=4, verbose_name='Percent')),
            ],
        ),
    ]
