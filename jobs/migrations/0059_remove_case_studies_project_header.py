# Generated by Django 4.0.2 on 2022-02-08 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0058_alter_case_studies_project_header'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case_studies',
            name='project_header',
        ),
    ]
