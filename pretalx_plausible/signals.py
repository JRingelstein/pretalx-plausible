from django.dispatch import receiver
from django.templatetags.static import static

from pretalx.orga.signals import html_head

from .models import PlausibleSettings


@receiver(html_head)
def plausible_url(sender, request, **kwargs):
    event = request.event if hasattr(request, "event") else None
    if not event:
        return ""
    try:
        settings = PlausibleSettings.objects.get(event=event)
        plausible_url = settings.plausible_url
    except PlausibleSettings.DoesNotExist:
        return ""

    if not plausible_url:
        return ""

    return f'<script async src="{plausible_url}"></script> <script src="{static("pretalx_plausible/plausible-init.js")}"></script>'
