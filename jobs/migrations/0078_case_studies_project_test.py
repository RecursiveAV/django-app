# Generated by Django 4.0.2 on 2022-03-14 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0077_case_studies_project_publish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_studies',
            name='project_test',
            field=models.BooleanField(blank=True, default=0, verbose_name='Is this ready to test (y/n)'),
        ),
    ]
