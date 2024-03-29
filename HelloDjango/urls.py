"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from cmdb import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('', views.welcome),
    path('home/', views.goHome),

    path('tech/', views.goTech),

    path('filmreview/', views.goFilmReview),
    path('filmreviewspeci', views.goFilmReviewSpeci),
    path('w/',views.goWrite),
    path('admin/', admin.site.urls),
]
