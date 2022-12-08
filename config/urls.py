"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Project imports
from user.views import UserModelViewSet
from laser.views import ClientsModelViewSet, PhotosModelViewSet, SessionsModelViewSet, TattoModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('tatto', TattoModelViewSet)
router.register('sessions', SessionsModelViewSet)
router.register('clients', ClientsModelViewSet)
router.register('Photos', PhotosModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
>>>>>>> 9a1fee9a3ee20432e5c241a05ed7a567b3ee7167
]
