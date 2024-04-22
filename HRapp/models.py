from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    age = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    # def __str__(self):
    #     if self.profile_picture:
    #         return self.profile_picture
    #     else:
    #         # Extracting initials from first and last names
    #         initials = ''.join(name[0].upper() for name in self.name.split())
    #         return initials
    