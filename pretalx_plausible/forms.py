from django import forms
from .models import PlausibleSettings


class PlausibleSettingsForm(forms.ModelForm):
    def __init__(self, *args, event=None, **kwargs):
        self.instance, _ = PlausibleSettings.objects.get_or_create(event=event)
        super().__init__(*args, **kwargs, instance=self.instance)

    class Meta:
        model = PlausibleSettings
        fields = ("plausible_url",)