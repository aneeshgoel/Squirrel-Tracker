from django.db import models

from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    AM = 'AM'
    PM = 'PM'

    Adult = 'ADULT'
    Juvenile = 'JUVENILE'

    AGE_CHOICES = (
            (Adult = 'ADULT'),
            (Juvenile = 'JUVENILE'),
        )

    TIME_CHOICES = (
            (AM = 'AM'),
            (PM = 'PM'),
        )

    BINARY_CHOICES = (
            (TRUE = 'TRUE'),
            (FALSE = 'FALSE'),
        )

    X = models.DecimalField(
            help_text=_('Longitutde of sighting'),
            max_length=10,
            max_digits=2,
            decimal_places=5,
        )

    Y = models.DecimalField(
            help_text=_('Latitude of sighting'),
            max_length=10,
            max_digits=2,
            decimal_places=5,
        )
    
    Hectare = models.CharField(
            help_text=_('ID tag; derived from hectare grid'),
            max_length=5,
        )

    Shift = models.CharField(
            help_text=_('Indication whether the sighting occurred in the afterrnoon or evening'),
            max_length=10,
            choices=TIME_CHOICES,
        )
    Date = models.DateField(
            help_text=_('Date of the sighting'),
        )

    Unique_squirrel_ID = models.CharField(
            help_text=_('Concatenation of Hectare(after deleting starting 0s) + Shift + first four digits of Date + Hectare squirrel number (after adding 0 in the bgeinning)'),
            max_length=20,
            primary_key=True,
        )

    Hectare_Squirrel_Number = IntegerField(
            help_text=_('Number within the chronological sequence of squirrel sightings for a discrete sighting session'),
            max_length=5,
            unique=False,
        )



            
