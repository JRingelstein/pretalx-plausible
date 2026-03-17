from django.db import models


class PlausibleSettings(models.Model):
    event = models.OneToOneField(
        to="event.Event",
        on_delete=models.CASCADE,
        related_name="plausible_url",
        null=True,
    )
    plausible_url = models.CharField(max_length=255)

    def __str__(self):
        event_str = str(self.event) if self.event else "No Event"
        return f"{event_str} - {self.plausible_url}"
