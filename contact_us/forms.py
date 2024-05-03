from django import forms
from django.core.validators import ValidationError

from contact_us.models import ContactUs


class ContactForm(forms.Form):
    text = forms.CharField(max_length=10, label='your message')
    name = forms.CharField(max_length=10, label='your name')

    def clean(self):
        text = self.cleaned_data.get('text')
        name = self.cleaned_data.get('name')

        if text == name:
            raise ValidationError('name and text are same!', code='text_and_same')

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if 'a' in text:
            raise ValidationError('a can not be in text', code='a_not')
        return text


class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'age', 'text',)