from django.db import models
from django import forms

# Create your models here.
class Userin(models.Model):
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.password + self.username + self.nickname


class UserinForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InformationFrorm(forms.Form):
    icon = forms.ImageField()
    nickname = forms.CharField()


class Informations(models.Model):
    nickname = models.CharField(max_length=20, blank=False)
    icon = models.ImageField(default='./Default/1.jpg', upload_to='./UserIcon')

