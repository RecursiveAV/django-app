# Generated by Django 4.0.2 on 2022-02-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0052_alter_case_studies_project_01_intro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_studies',
            name='project_01_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Section 01 image'),
        ),
    ]
