from django.db import models

# creating room model
class Room(models.Model):
    room_number = models.CharField(max_length=250, null= True)
    pictures = models.FileField(upload_to='images/')
    number_of_bed = models.CharField(max_length=250, default=1)
    cost = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=250, default='')