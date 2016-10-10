from django.db import models
from django import forms

K_A_P = (
    ('13', '年级:13'),
    ('14', '年级:14'),
    ('15', '年级:15'),
)


class User(models.Model):
    headImg = models.ImageField(upload_to='./Upload/')
    username = models.CharField(max_length=30, blank=False)
    kap = models.CharField(max_length=30, blank=False)
    C_lass = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
        return self.username + self.kap + self.C_lass


class UserForm(forms.Form):
    headImg = forms.ImageField()
    username = forms.CharField()
    kap = forms.ChoiceField(choices=K_A_P)
    C_lass = forms.CharField()



class Check(models.Model):
    headImg = models.CharField(max_length=999,blank=False)
    username = models.CharField(max_length=30, blank=False)
    kap = models.CharField(max_length=30, blank=False)
    C_lass = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
        return self.username + self.kap + self.C_lass + self.headImg


class CheckForm(forms.Form):
    headImg = forms.CharField()
    username = forms.CharField()
    kap = forms.ChoiceField(choices=K_A_P)
    C_lass = forms.CharField()


class Pinglun(models.Model):
    index = models.IntegerField()
    zan = models.IntegerField()
    cai = models.IntegerField()
    def __unicode__(self):
        return self.index + self.cai + self.zan



class Comment(models.Model):
    index = models.IntegerField()
    floor = models.IntegerField()
    pinglun = models.CharField(max_length=200)
    like = models.IntegerField()
    def __unicode__(self):
        return  self.floor + self.pinglun

class CommentForm(forms.Form):
    index = models.IntegerField()
    floor = models.IntegerField()
    pinglun = models.CharField()
    like = models.IntegerField()