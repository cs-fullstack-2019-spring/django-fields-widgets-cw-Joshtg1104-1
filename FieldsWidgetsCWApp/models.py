from django.db import models
from FieldsWidgetsCWApp.choices import STATUS_CHOICES, SUPERPOWER_CHOICES, ALIGNMENT_CHOICES


# Create your models here.

class SuperHeroModel(models.Model):
    name = models.CharField(max_length=60, default="")
    city_of_origin = models.CharField(max_length=100, default="")
    are_you_rich_or_have_superpowers = models.IntegerField(choices=STATUS_CHOICES, default=1)
    if_so_what_superpower = models.IntegerField(choices=SUPERPOWER_CHOICES, default=1)
    what_is_your_alignment = models.IntegerField(choices=ALIGNMENT_CHOICES, default=1)
    give_3_cases_in_which_you_used_your_powers = models.TextField(default="", max_length=3000)
