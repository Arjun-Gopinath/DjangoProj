from django.db import models

# Create your models here.
class GrocList(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    buy_date = models.DateField()
    #thumbnail

    def __str__(self):
        return self.name

# python manage.py makemigrations
# python manage.py migrate