# Generated by Django 4.0.2 on 2022-02-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0045_alter_case_studies_project_02_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_studies',
            name='project_03_main',
            field=models.CharField(max_length=850, null=True, verbose_name='03-The Challenge main text'),
        ),
        migrations.AlterField(
            model_name='case_studies',
            name='project_04_main',
            field=models.CharField(max_length=850, null=True, verbose_name='03-The Outcome main text'),
        ),
    ]
