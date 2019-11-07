"""djangopoems URL Configuration

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
from .views import PoemList, poem_detail, PoemCreate, PoemUpdate, PoemDelete

urlpatterns = [
    path('', PoemList.as_view(), name='poem_list'),
    path('create/', PoemCreate.as_view(), name='poem_create'),
    path('<slug>/', poem_detail, name='poem_detail'),
    path('<slug>/update', PoemUpdate.as_view(), name='poem_update'),
    path('<slug>/delete', PoemDelete.as_view(), name='poem_delete'),
]
