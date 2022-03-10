# Generated by Django 4.0.2 on 2022-02-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0026_rename_job_lab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, null=True, verbose_name='testimonial text')),
                ('name', models.CharField(max_length=300, null=True, verbose_name='name of person')),
                ('role', models.CharField(max_length=300, null=True, verbose_name='role or position')),
            ],
        ),
    ]