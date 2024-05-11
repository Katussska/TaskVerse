from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    founder = models.ForeignKey(User, related_name='founded_projects', on_delete=models.CASCADE)
    team = models.ManyToManyField(User, related_name='projects', blank=True)

    def __str__(self):
        return self.name
