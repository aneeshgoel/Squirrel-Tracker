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

    Gray = 'GRAY'
    Cinnamon = 'CINAMMON'
    Black = 'BLACK'


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

    COLOR_CHOICES = (
            (Gray = 'GRAY'),
            (Cinnamon = 'CINNAMON'),
            (Black  = 'BLACK'),
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

    Hectare_Squirrel_Number = model.IntegerField(
            help_text=_('Number within the chronological sequence of squirrel sightings for a discrete sighting session'),
            max_length=5,
            unique=False,
        )

    Age = models.CharField(
            help_text=_('Value is either Adult or Juvenile'),
            max_length=15,
            choices=AGE_CHOICES,
            null=True,
        )

    Primary_Fur_Color = models.CharField(
            help_text=_('Value is either gray, cinnamon or black'),
            max_length = 10,
            choices = COLOR_CHOICES,
            null = True
        )
    Highlight_Fur_Color = models.CharFirled(
            help_text=_(''),
            max_length - = 10,
            null = True,
            choices = COLOR_CHOICES,
        )

    Combination_of_Primary_and_Highlight_color = models.CharField(
            help_text=('Addition of primary and highlight fur color with a + sign'),
        )

    Color_Notes = models.CharField(
            help_text=_('Additional notes on color'),
            null = True,
        )

    GROUND_PLANE = 'GROUND PLANE'
    ABOVE_GROUND = 'ABOVE GROUND'

    LOCATION= (
            (GROUND_PLANE = 'GROUND PlANE'),
            (ABOVE_GROUND = 'ABOVE GROUND'),
        )

    Location = models.CharField(
            help_text=_('Either ground plabe or above ground depending on where the sighters located the squirrel'),
            choices = LOCATION,
            null = True,
            max_length = 20,
        )

    Above_Ground_Sighter_Measurement = models.CharField(
            help_text=_('If location is above ground then populate with False otherwise fill with a numeric value'),
            max_length = 10,
            null = True,
        )

    Specific_Location = models.CharField(
            help_text=_('Additional commentary on the squirrel location'),
            null = True,
        )

    Running = models.BooleanField(
            help_text=_('True if squirrel seen running; otherwise False'),
        )

    Chasing = models.BooleanField(











            
