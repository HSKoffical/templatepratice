from django import forms
from testapp.models import tempmodel
from django.core import validators
class tempform(forms.ModelForm):
    name = forms.CharField()
    roll = forms.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(100)])
    city = forms.CharField(validators=[validators.MinLengthValidator(3),validators.MaxLengthValidator(30)])
    feedbackform = forms.CharField()
    class Meta:
        model=tempmodel
        fields='__all__'
    def clean(self):
        value=super().clean()
        inputname=value['name']
        if len(inputname)<1:
            raise forms.ValidationError('please input name start with s')

        inputform=value['feedbackform']
        if len(inputform)<2:
            raise forms.ValidationError('please enter atleat to char')



