from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField(required = True)
    message = forms.CharField(widget=forms.Textarea, required = True)
