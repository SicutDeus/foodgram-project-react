import logging
import csv

from django.core.management.base import BaseCommand

from ingredients.models import Ingredient

class Command(BaseCommand):
    help = 'Импорт данных из csv в модель Ingredient'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help='Путь к файлу')

    def handle(self, *args, **options):
        logging.info('Заполнение модели Ingredient из csv запущено.')
        file_path = options['path'] + 'ingredients.csv'
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            ingredients = []
            for row in reader:
                try:
                    ingredient = Ingredient(
                    name=row[0],
                    measurement_unit=row[1],
                    )
                    ingredients.append(ingredient)
                except Exception as error:
                    logging.error(f'Ошибка в строке {row}: {error}')

            Ingredient.objects.bulk_create(ingredients, ignore_conflicts=True)

        logging.info('Заполнение модели Ingredient завершено.')