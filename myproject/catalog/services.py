import time
from django.core.cache import cache
from .models import Category


def get_cached_categories():
    """
    Получает список категорий с использованием кеша.
    """
    cache_key = 'categories'
    categories = cache.get(cache_key)

    if not categories:
        print("Fetching from database...")
        time.sleep(2)

        categories = list(Category.objects.all())
        cache.set(cache_key, categories, timeout=60 * 10)  # Кешируем на 10 минут

    return categories
