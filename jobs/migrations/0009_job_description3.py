# Generated by Django 4.0.2 on 2022-02-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_rename_description_job_description1_job_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description3',
            field=models.CharField(max_length=500, null=True, verbose_name='Conclusion text'),
        ),
    ]
