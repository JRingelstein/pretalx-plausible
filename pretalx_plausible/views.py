from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from pretalx.common.views.mixins import PermissionRequired

from .forms import PlausibleSettingsForm
from .models import PlausibleSettings


class PlausibleSettingsView(PermissionRequired, FormView):
    permission_required = "event.update_event"
    template_name = "pretalx_plausible/settings.html"
    form_class = PlausibleSettingsForm

    def get_success_url(self):
        return self.request.path

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["event"] = self.request.event
        return kwargs

    def get_object(self):
        return self.request.event

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        if action == "delete":
            try:
                settings = PlausibleSettings.objects.get(event=request.event)
                settings.delete()
                messages.success(
                    request, _("The plausible script url has been deleted.")
                )
            except PlausibleSettings.DoesNotExist:
                messages.warning(request, _("No plausible script url found to delete."))
            return redirect(self.get_success_url())

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("The plausible script url was updated."))
        return super().form_valid(form)
