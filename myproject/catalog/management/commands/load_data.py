from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Load data from fixtures'

    def handle(self, *args, **options):
        fixture_files = [
            'catalog/fixtures/categories.json',
            'catalog/fixtures/products.json'
        ]

        # Загрузка данных из фикстур
        for fixture in fixture_files:
            self.stdout.write(f"Loading fixture: {fixture}")
            call_command('loaddata', fixture)
        self.stdout.write(self.style.SUCCESS('Successfully loaded all fixtures.'))
