# Generated by Django 4.0.2 on 2022-02-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='file',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='videos'),
        ),
    ]
