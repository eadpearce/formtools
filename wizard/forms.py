from django import forms
from wizard.models import FlavourChoices, FrostingTypeChoices
from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Layout, Submit


class CakeStartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML.h1("Let's make a cake!"),
            Submit("submit", "Start"),
        )


class SpongeFlavourForm(forms.Form):
    sponge_flavour = forms.ChoiceField(
        choices=FlavourChoices.choices,
        widget=forms.RadioSelect,
        label="Sponge flavour",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "sponge_flavour",
            HTML.details("What is sponge cake?", "It's not like a kitchen sponge"),
            Submit("submit", "Next"),
        )


class FrostingTypeForm(forms.Form):
    frosting_type = forms.ChoiceField(
        choices=FrostingTypeChoices.choices,
        widget=forms.RadioSelect,
        label="Frosting type",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "frosting_type",
            HTML.details("What is frosting?", "Use google"),
            Submit("submit", "Next"),
        )


class FrostingFlavourForm(forms.Form):
    frosting_flavour = forms.ChoiceField(
        choices=FlavourChoices.choices,
        widget=forms.RadioSelect,
        label="Frosting flavour",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "frosting_flavour",
            Submit("submit", "Next"),
        )
