from formtools.wizard.views import NamedUrlSessionWizardView
from wizard import forms
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from wizard.models import Cake


class WizardView(NamedUrlSessionWizardView):
    form_list = [
        ("start", forms.CakeStartForm),
        ("sponge-flavour", forms.SpongeFlavourForm),
        ("frosting-type", forms.FrostingTypeForm),
        ("frosting-flavour", forms.FrostingFlavourForm),
    ]

    template_name = "wizard/form-step.html"

    def done(self, form_list, **kwargs):
        return redirect(reverse("cakes"))


class CakeListView(ListView):
    template_name = "wizard/cakes.html"

    def get_queryset(self):
        return Cake.objects.all()
