from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from myproject.catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модераторы" с необходимыми правами'

    def handle(self, *args, **kwargs):
        # Создание группы
        group, created = Group.objects.get_or_create(name='Модераторы')

        # Назначение прав
        product_ct = ContentType.objects.get_for_model(Product)
        permissions = [
            Permission.objects.get(codename='change_product', content_type=product_ct),
            Permission.objects.get(codename='can_unpublish_product', content_type=product_ct),
        ]

        group.permissions.set(permissions)
        self.stdout.write(self.style.SUCCESS('Группа "Модераторы" успешно создана и права назначены.'))
