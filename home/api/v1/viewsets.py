from django.conf import settings
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)

class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]
    permission_classes = [AllowAny]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""
    permission_classes = [AllowAny]
    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})



def home(request):
    return render(request, "home.html")


class WixViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "refresh_token",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token": settings.REFRESH_TOKEN
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        new_token = response.json()
        payload = {}
        headers = {
            'Authorization': new_token["access_token"],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }
        paging = request.data.get('paging', 'None')
        limit = request.data.get('limit', 'None')
        url = f"https://www.wixapis.com/blog/v3/categories?paging.offset={paging}&paging.limit={limit}"
        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)
        # return JsonResponse({'data': data_to_show})


class WixListPostViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "refresh_token",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token": settings.REFRESH_TOKEN
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        new_token = response.json()

        feature = request.data.get('featured', "None")
        headers = {
            'Authorization': new_token["access_token"],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }
        url = f"https://www.wixapis.com/blog/v3/posts?featured={feature}"
        response = requests.request("GET", url, headers=headers)

        data_to_show = response.json()
        return Response(data_to_show)
        # return JsonResponse({'list_post': data_to_show})


class WixListPostCategoriesViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "refresh_token",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token": settings.REFRESH_TOKEN
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        new_token = response.json()

        url = "https://www.wixapis.com/blog/v3/categories/query"

        payload = request.data

        headers = {
            'Authorization': new_token['access_token'],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show)
        # return JsonResponse({'post_cat': data_to_show})


class WixGetCategoriesViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "refresh_token",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token": settings.REFRESH_TOKEN
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        new_token = response.json()

        # categoryId = "b968e421-8c4a-40f1-9786-87155d62ff19"
        categoryId = request.data.get('categoryId', '')
        url = f"https://www.wixapis.com/blog/v3/categories/{categoryId}"

        payload = {}
        headers = {
            'Authorization': new_token['access_token'],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show)
        # return JsonResponse({'post_cat': data_to_show})


class WixListUpdateCategoriesViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "refresh_token",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token": settings.REFRESH_TOKEN
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        new_token = response.json()
        category = request.data.get('categoryid', '')

        url = f"https://www.wixapis.com/blog/v3/categories/{category}"

        payload = request.data
        try:
            payload.pop('categoryid')
        except:
            pass
        headers = {
            'Authorization': new_token['access_token'],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show)


class WixGetCategoriesBySlugViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "refresh_token",
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token": settings.REFRESH_TOKEN
        })
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        new_token = response.json()

        url = "https://www.wixapis.com/blog/v3/categories/slugs/{slug=test-category}"

        payload = {}
        headers = {
            'Authorization': new_token['access_token'],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show)
