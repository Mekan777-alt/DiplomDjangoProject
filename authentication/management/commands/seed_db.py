from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from authentication.enum import Groups


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.seed_groups()


    def seed_groups(self):
        Group.objects.get_or_create(name=Groups.DECANAT.name)
        Group.objects.get_or_create(name=Groups.STUDENT.name)
        Group.objects.get_or_create(name=Groups.TEACHER.name)

        self.stdout.write('Groups added to database')
