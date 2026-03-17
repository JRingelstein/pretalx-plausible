from django.dispatch import receiver

from pretalx.orga.signals import html_head
from .models import PlausibleSettings


@receiver(html_head)
def plausible_url(sender, request, **kwargs):
    event = request.event if hasattr(request, 'event') else None
    if not event:
        return ""
    try:
        settings = PlausibleSettings.objects.get(event=event)
        plausible_url = settings.plausible_url
    except PlausibleSettings.DoesNotExist:
        return ""
    
    if not plausible_url:
        return ""
    
    return f'<script async src="{plausible_url}"></script> <script unsafe-inline>window.plausible=window.plausible||function(){{(plausible.q=plausible.q||[]).push(arguments)}},plausible.init=plausible.init||function(i){{plausible.o=i||{{}}}};plausible.init()</script>'