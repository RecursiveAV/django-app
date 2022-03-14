# Generated by Django 4.0.2 on 2022-03-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0076_case_studies_project_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_studies',
            name='project_publish',
            field=models.BooleanField(blank=True, default=0, verbose_name='Is this ready to publish (y/n)'),
        ),
        migrations.AlterField(
            model_name='case_studies',
            name='project_complete',
            field=models.BooleanField(blank=True, default=0, verbose_name='Is this Case Study Complete? (y/n)'),
        ),
    ]