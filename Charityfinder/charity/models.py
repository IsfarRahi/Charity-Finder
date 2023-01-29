from django.db import models


# Create your models here.

class Charity(models.Model):
    charity_name = models.CharField(max_length=25)
    total_volunteer = models.IntegerField()
    monthly_donation = models.IntegerField()
    email = models.EmailField(max_length=20)
    phn_number = models.IntegerField()

    class Meta:
        db_table = "charity"