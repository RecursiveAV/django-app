# Generated by Django 4.0.2 on 2022-02-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0042_case_studies_project_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_studies',
            name='project_category',
            field=models.CharField(max_length=130, null=True, verbose_name='project category (content/AV/acoustics/development/experiential/retail)'),
        ),
    ]
