# Generated by Django 4.0.2 on 2022-02-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0035_header_videos'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('av', models.ImageField(null=True, upload_to='images/', verbose_name='av image')),
                ('acoustics', models.ImageField(null=True, upload_to='images/', verbose_name='acoustics image')),
                ('software', models.ImageField(null=True, upload_to='images/', verbose_name='software image')),
                ('lighting', models.ImageField(null=True, upload_to='images/', verbose_name='lighting image')),
            ],
        ),
    ]
