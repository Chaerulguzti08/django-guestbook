"""
URL configuration for guestbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from appguestbook.views import EventGet, EventPost, EventPut, EventDetailGet, EventDelete, GuestGet, GuestDetailGet, GuestPost, GuestPut, GuestDelete, GuestDetailByEventGet, index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path('api/event/', EventGet.as_view()),
    path('api/event/detail/<int:id>/', EventDetailGet.as_view()),
    path('api/event/create/', EventPost.as_view()),
    path('api/event/delete/<int:id>/', EventDelete.as_view()),
    path('api/event/edit/<int:id>/', EventPut.as_view()),

    path('api/guest/', GuestGet.as_view()),
    path('api/guest/detail/<int:id>/', GuestDetailGet.as_view()),
    path('api/guest/detail/event/<int:id>/', GuestDetailByEventGet.as_view()),
    path('api/guest/create/', GuestPost.as_view()),
    path('api/guest/delete/<int:id>/', GuestDelete.as_view()),
    path('api/guest/edit/<int:id>/', GuestPut.as_view()),
]
