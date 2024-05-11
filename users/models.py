from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures')

    def __str__(self):
        return self.name
