import environ.environ
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings


def home(request):
    return render(request, "home.html")


class WixViewSet(APIView):
    # renderer_classes = [TemplateHTMLRenderer]

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

        url = "https://www.wixapis.com/blog/v3/categories?paging.offset=2&paging.limit=3"

        payload = {}
        headers = {
            'Authorization': new_token["access_token"],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)
        # return JsonResponse({'data': data_to_show})


class WixListPostViewSet(APIView):
    # renderer_classes = [TemplateHTMLRenderer]

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

        url = "https://www.wixapis.com/blog/v3/posts?featured=True"

        payload = {}
        headers = {
            'Authorization': new_token["access_token"],
            'Accept': 'application/json',
            'Cookie': 'XSRF-TOKEN=1671128033|Rh5N7XXpQIPm'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show)
        # return JsonResponse({'list_post': data_to_show})


class WixListPostCategoriesViewSet(APIView):
    # renderer_classes = [TemplateHTMLRenderer]

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

        url = "https://www.wixapis.com/blog/v3/categories/query"

        payload = {
            "paging": {"limit": 6},
            "filter": {"title": "summer"},
            "sort": [],
            "fieldsToInclude": ["Unknown", "New Category"]
        }
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
    # renderer_classes = [TemplateHTMLRenderer]

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

        categoryId = "b968e421-8c4a-40f1-9786-87155d62ff19"

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


class WixGetCategoriesBySlugViewSet(APIView):
    # renderer_classes = [TemplateHTMLRenderer]

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
