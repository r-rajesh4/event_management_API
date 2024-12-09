from django.db import models

# Create your models here.
class User(models.Model):
    ADMIN = 'admin'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=USER)

    def __str__(self):
        return self.username
    
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.id} for {self.event.name}"