# Generated by Django 4.0.2 on 2022-02-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_job_description3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description2',
            field=models.CharField(max_length=500, null=True, verbose_name='Secondary description text'),
        ),
    ]
