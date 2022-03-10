# Generated by Django 4.0.2 on 2022-02-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0030_awards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_image', models.ImageField(null=True, upload_to='images/', verbose_name='team image')),
            ],
        ),
        migrations.AlterField(
            model_name='awards',
            name='link',
            field=models.CharField(max_length=250, null=True, verbose_name='link'),
        ),
    ]
