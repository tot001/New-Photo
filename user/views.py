from django.shortcuts import render, render_to_response

# Create your views here.



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import *
from django.shortcuts import render

from .models import *


def SignUp(request):
    if request.method == "POST":
        db = UserinForm(request.POST, request.FILES)
        if db.is_valid():
            username = db.cleaned_data['username']
            password = db.cleaned_data['password']
            user = Userin()
            user.username = username
            user.password = password
            user.save()
            return HttpResponse('already Sign Up')
    else:
        db = UserinForm()
    return render(request, 'SignUp.html', {'db': db})


def SignIn(request):
    if request.method == "POST":
        db = UserinForm(request.POST, request.FILES)
        if db.is_valid():
            username = db.cleaned_data['username']
            password = db.cleaned_data['password']

            user = Userin.objects.filter(username__exact=username, password__exact=password)
            if user:
                response = HttpResponseRedirect('/index')
                response.set_cookie('username', username, 360000)
                return response
            else:
                return render(request, 'message.html')
    else:
        db = UserinForm()
    return render(request, 'SignIn.html', {'db': db})



def index(request):
    username = request.COOKIES.get('username')
    return render(request,'UserIndex.html', {'username':username})

