# forms.py
from django import forms
from .models import Contact, Subscriber, FavoriteGame

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'gamer_tag']

class FavoriteGameForm(forms.ModelForm):
    class Meta:
        model = FavoriteGame
        fields = ['created_by', 'title', 'genre', 'description']
