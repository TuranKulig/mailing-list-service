"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

from mailing.views import ClientViewSet, MailingViewSet, MessageViewSet
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'message', MessageViewSet)
router.register(r'mailing', MailingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mailing/', include(router.urls)),
    path("refresh/", TokenRefreshView.as_view()),
    path("obtain/", TokenObtainPairView.as_view()),


]
urlpatterns += doc_urls
