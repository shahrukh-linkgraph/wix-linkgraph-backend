from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path("", home, name="home"),
    path("data/", WixViewSet.as_view(), name='data'),
    path('list_post/', WixListPostViewSet.as_view(), name='list_post'),
    path('post_cat/', WixListPostCategoriesViewSet.as_view(), name='post_cat'),
    path('get_category/', WixListPostCategoriesViewSet.as_view(), name='get_category'),
    path('get_category_slug/', WixGetCategoriesBySlugViewSet.as_view(), name='post_cat'),
    path('patch_category/', WixListUpdateCategoriesViewSet.as_view(), name='patch_category')
]
