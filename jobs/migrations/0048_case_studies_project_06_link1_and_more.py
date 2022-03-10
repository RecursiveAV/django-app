# Generated by Django 4.0.2 on 2022-02-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0047_alter_case_studies_project_02_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_studies',
            name='project_06_link1',
            field=models.CharField(max_length=120, null=True, verbose_name='06 - manufacturer 1'),
        ),
        migrations.AddField(
            model_name='case_studies',
            name='project_06_link2',
            field=models.CharField(max_length=120, null=True, verbose_name='06 - manufacturer 2'),
        ),
        migrations.AlterField(
            model_name='case_studies',
            name='project_05_link3',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='05 - link 3'),
        ),
    ]