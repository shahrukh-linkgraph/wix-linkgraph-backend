from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet, WixViewSet, WixListPostViewSet, WixListPostCategoriesViewSet, WixGetCategoriesViewSet,
    WixListUpdateCategoriesViewSet, WixCreateDraftPostViewSet, WixListCreateCategoriesViewSet,
    WixGetSiteBusinessViewSet, WixListMemberListViewSet, WixGetMemberListViewSet, WixCreateMembersViewSet,
    SearchAtlasRegistrationApi, SearchAtlasLoginApi, SearchAtlasCreateProjectApi, WixAccountLevelSiteProperties,
    CreateCustomerLogin, RegisterWithMember, WixListDraftPostViewSet, GetToken
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
    path('create_draft_post/', WixCreateDraftPostViewSet.as_view(), name='create_draft_post'),
    path('get_site_properties/', WixGetSiteBusinessViewSet.as_view(), name='get_site_properties'),
    path('list_members/', WixListMemberListViewSet.as_view(), name='list_members'),
    path('get_members/', WixGetMemberListViewSet.as_view(), name='list_members'),
    path('create_members/', WixCreateMembersViewSet.as_view(), name='create_members'),
    path('customer_registration/', SearchAtlasRegistrationApi.as_view(), name='customer_registration'),
    path('customer_login/', SearchAtlasLoginApi.as_view(), name='customer_login'),
    path('create_project/', SearchAtlasCreateProjectApi.as_view(), name='create_project'),
    path('account_level/site_properties/', WixAccountLevelSiteProperties.as_view(), name='account_level'),
    path('create_customer_login/', CreateCustomerLogin.as_view(), name='newlogincustomer'),
    path('member_register/', RegisterWithMember.as_view(), name='member_register'),
    path('list_draft_post/', WixListDraftPostViewSet.as_view(), name='list_draft_post'),
    path('get_token/', GetToken.as_view(), name='get_token'),
]
