from django import forms
from .models import Customer, GENDER_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CustomerForms(forms.ModelForm):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES,
    #                            widget=forms.RadioSelect,
    #                            initial='male')

    class Meta:
        model = Customer
        exclude = ['updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.attrs = {
            'novalidate': ''
        }
        self.helper.add_input(Submit('save_customer', 'Save Customer'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-danger'))
