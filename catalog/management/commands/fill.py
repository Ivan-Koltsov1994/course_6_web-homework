from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Привет! Заполняем базу начальными значениями")
        products_list = [
            {
                "name": "манго",
                "description": "плоды растений рода Манго семейства Анакардиевые",
                "category": "фрукты",
                "unit_price": 170,
                "creation_date": "2022-07-10",
                "modified_date": "2023-05-14"
            },
            {
                "name": "Сыр",
                "description": "Однолетнее травянистое растение, вид рода Огурец семейства Тыквенные, овощная культура",
                "category": "овощи",
                "unit_price": 116,
                "creation_date": "2022-04-16",
                "modified_date": "2023-05-14"
            },
        ]

        products_objects = []
        for item in products_list:
            products_objects.append(Product(**item))

        Product.objects.bulk_create(products_objects)