from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {
                "name": "манго",
                "description": "плоды растений рода Манго семейства Анакардиевые",
                "category": "фрукты",
                "price": 170,
                "date_of_creation": "2022-07-10 11:00",
                "date_of_change": "2022-05-24 20:15"
            },
            {
                "name": "Сыр",
                "description": "Однолетнее травянистое растение, вид рода Огурец семейства Тыквенные, овощная культура",
                "category": "овощи",
                "price": 116,
                "date_of_creation": "2022-04-16 19:00",
                "date_of_change": "2022-05-14 20:17"
            },
        ]

        products_objects = []
        for item in products_list:
            products_objects.append(Product(**item))

        Product.objects.bulk_create(products_objects)