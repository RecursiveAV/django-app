# Generated by Django 4.0.2 on 2022-02-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0033_remove_contact_address_contact_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='building',
            field=models.CharField(max_length=100, null=True, verbose_name='street name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(max_length=150, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postcode',
            field=models.CharField(max_length=150, null=True, verbose_name='postcode'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street',
            field=models.CharField(max_length=150, null=True, verbose_name='street name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(max_length=100, null=True, verbose_name='telephone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='town',
            field=models.CharField(max_length=150, null=True, verbose_name='town and county'),
        ),
    ]
