from django.db import models
from society.models import Flat

class User(models.Model):
    ROLE_CHOICES = [
        ('resident', 'Resident'),
        ('guardian', 'Guardian'),
        ('volunteer', 'Volunteer'),
        ('security', 'Security'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    flat = models.ForeignKey(
        Flat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name