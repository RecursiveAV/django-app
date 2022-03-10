# Generated by Django 4.0.2 on 2022-02-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0069_alter_lab_description1_alter_lab_description2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='summary',
        ),
        migrations.AddField(
            model_name='lab',
            name='main_summary',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Main Summary text'),
        ),
        migrations.AddField(
            model_name='lab',
            name='sub_summary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Sub Summary text'),
        ),
    ]