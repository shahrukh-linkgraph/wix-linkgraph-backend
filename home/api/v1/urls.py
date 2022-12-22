from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet, WixViewSet, WixListPostViewSet, WixListPostCategoriesViewSet, WixGetCategoriesViewSet,
    WixListUpdateCategoriesViewSet,
)
from home.views import home

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")

urlpatterns = [
    path("", include(router.urls)),
    path("", home, name="home"),
    path("data/", WixViewSet.as_view(), name='data'),
    path('list_post/', WixListPostViewSet.as_view(), name='list_post'),
    path('post_cat/', WixListPostCategoriesViewSet.as_view(), name='post_cat'),
    path('get_category/', WixGetCategoriesViewSet.as_view(), name='get_category'),
    path('patch_category/', WixListUpdateCategoriesViewSet.as_view(), name='patch_category')
]
