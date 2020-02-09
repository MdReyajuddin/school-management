from django import forms
from schooladmin.models import Students, Index, Contact

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)