"""dialoguescafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from events.views import get_index, EventListView, EventDetailView, EventCreateView ,EventDeleteView, EventUpdateView
from accounts.views import login
from accounts.views import register
from accounts.views import signout
from accounts.views import profile




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', get_index),
    path('login/',login),
    path('register/', register),
    path('logout/', signout),
    path('profile/', profile),
    url(r'^list/$',EventListView.as_view(),name='list'),
    url(r'^list/(?P<pk>\d+)/$',EventDetailView.as_view(),name='detail'),
    url(r'^create/$',EventCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',EventUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',EventDeleteView.as_view(),name='delete'),

    ]
