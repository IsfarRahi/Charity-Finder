# Generated by Django 4.1.5 on 2023-01-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_alter_charity_monthly_donation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='charity_name',
            field=models.CharField(max_length=20),
        ),
    ]
