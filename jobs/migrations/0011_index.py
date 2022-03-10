# Generated by Django 4.0.2 on 2022-02-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_job_description2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Introtext', models.CharField(max_length=200, null=True, verbose_name='Main Intro text')),
                ('Introimage', models.ImageField(null=True, upload_to='images/', verbose_name='Main Image')),
            ],
        ),
    ]
