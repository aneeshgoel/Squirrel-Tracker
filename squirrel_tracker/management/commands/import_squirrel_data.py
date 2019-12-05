import csv

from django.core.management.base import BaseCommand

from squirrel_tracker.models import Squirrel


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        Squirrel.objects.all().delete()   #Deleting dummy squirrels before importing
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            s = Squirrel(
                X=item['X'],
                Y=item['Y'],
                Shift=item['Shift'],
                Date=item['Date'],
                Unique_squirrel_ID=item['Unique Squirrel ID'],
                Age=item['Age'],
                Primary_Fur_Color=item['Primary Fur Color'],
                Location=item['Location'],
                Specific_Location=item['Specific Location'],
                Running=item['Running'],
                Chasing=item['Chasing'],
                Climbing=item['Climbing'],
                Eating=item['Eating'],
                Foraging=item['Foraging'],
                Other_Activities=item['Other Activities'],
                Kuks=item['Kuks'],
                Quaas=item['Quaas'],
                Moans=item['Moans'],
                Tail_flags=item['Tail flags'],
                Tail_twitching=item['Tail twitches'],
                Approaches=item['Approaches'],
                Indifferent=item['Indifferent'],
                Runs_from=item['Runs from'],
            )
            s.save()
