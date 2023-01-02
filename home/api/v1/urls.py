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
    path("list_categories/", WixViewSet.as_view(), name='data'),
    path('list_posts/', WixListPostViewSet.as_view(), name='list_post'),
    path('post_categories/', WixListPostCategoriesViewSet.as_view(), name='post_cat'),
    path('create_categories/', WixListCreateCategoriesViewSet.as_view(), name='create_categories'),
    path('get_categories/', WixGetCategoriesViewSet.as_view(), name='get_category'),
    path('patch_categories/', WixListUpdateCategoriesViewSet.as_view(), name='patch_category'),
    path('create_draft_post/', WixCreateDraftPostViewSet.as_view(), name='create_draft_post')
]
