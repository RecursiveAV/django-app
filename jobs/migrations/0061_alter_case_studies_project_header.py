# Generated by Django 4.0.2 on 2022-02-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0060_case_studies_project_header_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_studies',
            name='project_header',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='case study header image'),
        ),
    ]
