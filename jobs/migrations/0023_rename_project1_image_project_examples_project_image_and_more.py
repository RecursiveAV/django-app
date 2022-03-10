# Generated by Django 4.0.2 on 2022-02-06 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0022_project_examples_project1_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project_examples',
            old_name='project1_image',
            new_name='project_image',
        ),
        migrations.RenameField(
            model_name='project_examples',
            old_name='project1_size',
            new_name='project_size',
        ),
        migrations.RenameField(
            model_name='project_examples',
            old_name='project1_text',
            new_name='project_text',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project2_image',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project2_text',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project3_image',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project3_text',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project4_image',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project4_text',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project5_image',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project5_text',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project6_image',
        ),
        migrations.RemoveField(
            model_name='project_examples',
            name='project6_text',
        ),
    ]