from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Room(models.Model):
    Room_Types={
        ('Deluxe','Deluxe Room'),
        ('Executive','Executive Suite'),
        ('King','King Suite'),
        ('Queen','Queen Suite'),
        ('Luxury','Luxury Suite'),
    }
    room_number=models.IntegerField()
    room_category=models.CharField(max_length=20, choices=Room_Types)
    beds=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return f'{self.room_number}. is a {self.room_category} with {self.beds} costing {self.price}'

class Booking(models.Model):
    Room_Types_Available={
        ('Deluxe','Deluxe Room'),
        ('Executive','Executive Suite'),
        ('King','King Suite'),
        ('Queen','Queen Suite'),
        ('Luxury','Luxury Suite'),
    }
    room_type=models.CharField(max_length=20, choices=Room_Types_Available)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    Number_of_Adults=models.IntegerField()
    Number_of_Children=models.IntegerField()
    Email=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    CNIC = models.IntegerField()
    Contact_Number = models.IntegerField()
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

