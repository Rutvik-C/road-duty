from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.


class Rider(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Challan(models.Model):
    rider = models.ForeignKey(Rider, on_delete=CASCADE)
    license_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    date_time = models.DateTimeField(editable=False, null=True, blank=True)
    locations = models.CharField(max_length=50)
    # image_url = models.IntegerField(default=100)

    def __str__(self):
        return str(self.license_number)


class Query(models.Model):
    challan = models.ForeignKey(Challan,  on_delete=CASCADE)
    issue = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.issue)


class ChallanImage(models.Model):
    challan = models.ForeignKey(Challan, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="images/")


"""
Challans
- cid (primary key)
- rid (foreign key)
- license_number
- image_url
- status
- amount
- datetime
- location

Rider
- rid (primary key)
- name
- phone
- email

Query
- cid (foreign key)
- issue
- status

"""
