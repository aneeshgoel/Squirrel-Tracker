from django.db import models

from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):

    TRUE = 'TRUE'
    FALSE = 'FALSE'

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



            
            
