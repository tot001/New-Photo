"""photo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from django.contrib import admin

from django.conf.urls.static import static
from graph import views as view
from photo import settings

urlpatterns = [
                  url(r'^$', view.index),
                  url(r'^zan/', view.zan),
                  url(r'^cai/', view.cai),
                  url(r'^searchuser/', view.uploadsearch),
                  url(r'^userlist/', view.uploadlist),
                  url(r'^upload/', view.Upload),
                  url(r'^check/', view.Checked),
                  url(r'^search/', view.search),
                  url(r'^in/', view.inside_view),
                  url(r'^hot/', view.hot),
                  url(r'^ajaxindex/', view.ajaxindex),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
