# Generated by Django 4.1.5 on 2023-01-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_alter_charity_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='monthly_donation',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charity',
            name='phn_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='charity',
            name='total_volunteer',
            field=models.IntegerField(),
        ),
    ]
