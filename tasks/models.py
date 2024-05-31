from django.db import models
from projects.models import Project
from projects.models import User


class Tag(models.Model):
    DEFAULT_TAGS = [
        ('Bug', 'Bug'),
        ('Enhancement', 'Enhancement'),
        ('Feature', 'Feature'),
    ]

    COLOR_MAP = {
        'Bug': 'Red',
        'Enhancement': 'Green',
        'Feature': 'Blue',
    }

    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Purple', 'Purple'),
        ('Pink', 'Pink'),
        ('Grey', 'Grey'),
    ]

    name = models.CharField(max_length=100, choices=DEFAULT_TAGS, blank=True)
    custom_name = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.custom_name:
            return self.custom_name
        else:
            return 'Unnamed Tag'

    def save(self, *args, **kwargs):
        if self.name and not self.color:
            self.color = self.COLOR_MAP.get(self.name, 'Grey')
        super().save(*args, **kwargs)


class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending'
        IN_PROGRESS = 'In progress'
        DONE = 'Done'

    class Priority(models.TextChoices):
        NONE = 'None'
        LOW = 'Low'
        NORMAL = 'Normal'
        HIGH = 'High'
        URGENT = 'Urgent'

    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(
        max_length=100,
        choices=Priority.choices,
        default=Priority.NONE
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='tasks',
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.PENDING
    )
    completion_date = models.DateTimeField(
        null=True,
        blank=True
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    assigned_to = models.ForeignKey(
        User,
        related_name='assigned_tasks',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
