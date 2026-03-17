from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PlausibleApp(AppConfig):
    name = "pretalx_plausible"
    verbose_name = "pretalx plausible plugin"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx plausible plugin")
        author = "Jessica Ringelstein"
        description = gettext_lazy("pretalx plugin for pretalx plausible plugin")
        visible = True
        version = __version__
        category = "OTHER"
        settings_links = [
            (gettext_lazy("Settings"), "plugins:pretalx_plausible:settings", {})
        ]

    def ready(self):
        from . import signals  # noqa: PLC0415, F401

default_app_config = "pretalx_plausible.PlausibleApp"