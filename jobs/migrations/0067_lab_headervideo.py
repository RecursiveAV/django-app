# Generated by Django 4.0.2 on 2022-02-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0066_alter_case_studies_project_01_intro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='headervideo',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='Header video'),
        ),
    ]