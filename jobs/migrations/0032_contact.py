# Generated by Django 4.0.2 on 2022-02-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0031_team_alter_awards_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='address')),
                ('email', models.CharField(max_length=250, null=True, verbose_name='email')),
                ('telephone', models.CharField(max_length=250, null=True, verbose_name='telephone')),
            ],
        ),
    ]