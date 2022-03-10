# Generated by Django 4.0.2 on 2022-02-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0023_rename_project1_image_project_examples_project_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_examples',
            name='project_services',
            field=models.CharField(max_length=130, null=True, verbose_name='project services (Software/Acoustics/AV Design)'),
        ),
        migrations.AlterField(
            model_name='project_examples',
            name='project_image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='project image'),
        ),
        migrations.AlterField(
            model_name='project_examples',
            name='project_size',
            field=models.CharField(max_length=130, null=True, verbose_name='project size (-big/-wide/-horizontal or - for standard)'),
        ),
        migrations.AlterField(
            model_name='project_examples',
            name='project_text',
            field=models.CharField(max_length=130, null=True, verbose_name='project text'),
        ),
    ]
