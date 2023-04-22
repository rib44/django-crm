from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.models.CharField(max_length=50)
    last_name = models.models.CharField(max_length=50)
    email = models.models.CharField(max_length=100)
    phone = models.models.CharField(max_length=15)
    address = models.models.CharField(max_length=100)
    city = models.models.CharField(max_length=50)
    state = models.models.CharField(max_length=50)
    zipcode = models.models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

