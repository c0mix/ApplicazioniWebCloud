"""italiasport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from rest_framework.routers import DefaultRouter
from sito.views import SportivoViewSet, AttivitaViewSet, UserViewSet, TestViewSet
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from djoser import views

router = DefaultRouter()
router.register(prefix='sportivi', viewset=SportivoViewSet)
router.register(prefix='attivita', viewset=AttivitaViewSet)
router.register(prefix='tests', viewset=TestViewSet)
router.register(prefix='users', viewset=UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/login', obtain_jwt_token),  # using JSON web token
    url(r'^auth/register', views.RegistrationView.as_view()),
    url(r'^auth/password/reset', views.PasswordResetView.as_view()),
    url(r'^auth/password/reset/confirm', views.PasswordResetConfirmView.as_view()),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/logout/$', views.LogoutView.as_view(), name='logout'),
]