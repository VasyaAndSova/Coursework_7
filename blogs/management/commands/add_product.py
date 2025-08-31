from django.core.management import call_command
from django.core.management.base import BaseCommand

from blogs.models import Blog


class Command(BaseCommand):
    help = "Add blogs to the database"

    def handle(self, *args, **options):
        Blog.objects.all().delete()

        call_command("loaddata", "blogs.json")

        self.stdout.write(self.style.SUCCESS("Successfully loaded blogs from fixtures."))
