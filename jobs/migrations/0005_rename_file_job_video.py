# Generated by Django 4.0.2 on 2022-02-05 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_alter_job_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='file',
            new_name='video',
        ),
    ]
