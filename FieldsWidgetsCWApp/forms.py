from django import forms
from .models import SuperHeroModel
from FieldsWidgetsCWApp.choices import STATUS_CHOICES, SUPERPOWER_CHOICES, ALIGNMENT_CHOICES


class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHeroModel
        fields = "__all__"
        widgets = {
            "are_you_rich_or_have_superpowers": forms.Select(choices=STATUS_CHOICES),
            "if_so_what_superpower": forms.Select(choices=SUPERPOWER_CHOICES),
            "what_is_your_alignment": forms.Select(choices=ALIGNMENT_CHOICES),
        }
