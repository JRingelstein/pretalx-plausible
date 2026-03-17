from django.db import models


class PlausibleSettings(models.Model):
    event = models.OneToOneField(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="plausible_url",
        null= True,
    )
    plausible_url = models.CharField(max_length=255)
