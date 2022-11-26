from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
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
    status = models.CharField(
        max_length=50,
        choices=(("unpaid", "unpaid"),
                 ("to_check_manually", "to_check_manually"),
                 ("query_raised", "query_raised"),
                 ("paid", "paid")),
        default="unpaid")
    amount = models.IntegerField(default=2000, null=True, blank=True)
    date_time = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=50)
    # image_url = models.IntegerField(default=100)

    def __str__(self):
        return str(self.license_number)


class Query(models.Model):
    challan = models.ForeignKey(Challan, on_delete=CASCADE)
    issue = models.CharField(max_length=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.issue)


class ChallanImage(models.Model):
    challan = models.ForeignKey(Challan, on_delete=models.CASCADE, default=1)
    type = models.CharField(max_length=50, choices=(
        ("whole", "whole"), ("cutout", "cutout"), ("bulk", "bulk")), default="bulk")
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
