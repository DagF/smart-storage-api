"""idi_asset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views

from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "<h1>Smart Storage Server</h1>" +
        "<ul>"+
        "<li><a href='/admin/'>admin</a></li>" +
        "<li><a href='/api/'>api</a></li>"
        "<li><a href='#'>frontend</a></li>"
        "<ul/>"
    )

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api/auth/', views.obtain_auth_token),
]
