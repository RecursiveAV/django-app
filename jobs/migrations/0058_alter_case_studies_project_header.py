# Generated by Django 4.0.2 on 2022-02-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0057_delete_shippinginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_studies',
            name='project_header',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='case study header video'),
        ),
    ]
