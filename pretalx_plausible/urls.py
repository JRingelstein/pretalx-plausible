from django.urls import re_path

from pretalx.event.models.event import SLUG_REGEX

from .views import PlausibleSettingsView

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/settings/p/pretalx_plausible/$",
        PlausibleSettingsView.as_view(),
        name="settings",
    )
]
