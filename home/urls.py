from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
#
# from home.views import WixViewSet
#
# router = DefaultRouter()
# router.register('data', WixViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("data/", WixViewSet.as_view(), name='data'),
    path('list_post/', WixListPostViewSet.as_view(), name='list_post'),
    path('post_cat/', WixListPostCategoriesViewSet.as_view(), name='post_cat')
]
