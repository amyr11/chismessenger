from django import forms
from .models import Chismis


class AddChismisForm(forms.ModelForm):
    chismis = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Mare, anong latest?",
                "rows": "3",
            }
        )
    )

    class Meta:
        model = Chismis
        fields = ["chismis"]
