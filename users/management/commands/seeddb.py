from django.core.management.base import BaseCommand
from django.db import DatabaseError

from projects.models import Project
from tasks.models import Task
from users.models import User


class Command(BaseCommand):
    help = 'Seed the DB'

    def handle(self, *args, **options):
        usernames = ['boleslav', 'spytihnev', 'borivoj', 'cestmir', 'vratislav']
        users = []
        projects = []

        for username in usernames:
            try:
                users.append(User.objects.create(
                    username=username,
                    password='kokos-123',
                    email=f'{username}@example.com'
                ))
            except DatabaseError as e:
                self.stdout.write(self.style.ERROR(str(e)))
        self.stdout.write(self.style.SUCCESS('Seeding users done'))

        try:
            projects = [
                Project.objects.create(
                    name='Olomoucka vrazda',
                    description='Vaclav je fakt zmrd',
                    founder=users[1]
                ),
                Project.objects.create(
                    name='Projekt 2',
                    description='Lorem impsum jsem popis projektu',
                    founder=users[1]
                ),
                Project.objects.create(
                    name='Projekt 3',
                    description='Lorem impsum jsem popis projektu',
                    founder=users[0]
                ),
            ]
            self.stdout.write(self.style.SUCCESS('Seeding projects done'))
        except DatabaseError as e:
            self.stdout.write(self.style.ERROR(str(e)))

        for project in projects:
            for i in range(5):
                try:
                    Task.objects.create(
                        name=f'Task {i}',
                        description=f'task {i}',
                        project=project
                    )
                except DatabaseError as e:
                    self.stdout.write(self.style.ERROR(str(e)))
        self.stdout.write(self.style.SUCCESS('Seeding tasks done'))
