from allauth.utils import generate_unique_username
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
    UserSerializer, CreateCustomerLoginSerializer,
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
        url = "https://www.wixapis.com/blog/v3/categories"
        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)


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
        return Response(data_to_show, status=status.HTTP_200_OK)


class WixListCreateCategoriesViewSet(APIView):
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

        url = "https://www.wixapis.com/blog/v3/categories"

        payload = json.dumps(request.data)
        headers = {
            'Authorization': new_token['access_token'],
            'Content-Type': 'application/json',
            'Cookie': 'XSRF-TOKEN=1672142769|-9a_FxvDMnoW'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return Response(response.json(), status=status.HTTP_201_CREATED)


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
        return Response(data_to_show, status=status.HTTP_201_CREATED)


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
        return Response(data_to_show, status=status.HTTP_200_OK)


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

        payload = json.dumps(
            request.data
        )
        headers = {
            'Authorization': new_token['access_token'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Cookie': 'XSRF-TOKEN=1672142769|-9a_FxvDMnoW'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)


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
        return Response(data_to_show, status=status.HTTP_200_OK)


class WixCreateDraftPostViewSet(APIView):
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
        import requests
        import json

        url = "https://www.wixapis.com/blog/v3/draft-posts"

        payload = json.dumps(request.data)
        headers = {
            'Authorization': new_token['access_token'],
            'Content-Type': 'application/json',
            'Cookie': 'XSRF-TOKEN=1672415706|nnA264JF4vGe'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_201_CREATED)


class WixGetSiteBusinessViewSet(APIView):
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

        url = "https://www.wixapis.com/site-properties/v4/properties"

        payload = {}
        headers = {
            'Authorization': new_token['access_token'],
            'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)


class WixListMemberListViewSet(APIView):
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

        url = "https://www.wixapis.com/members/v1/members"

        payload = {}
        headers = {
            'Authorization': new_token['access_token'],
            'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)


class WixGetMemberListViewSet(APIView):
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
        id = request.data.get('id')
        url = f"https://www.wixapis.com/members/v1/members/{id}"

        payload = {}
        headers = {
            'Authorization': new_token['access_token'],
            'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_200_OK)


class WixCreateMembersViewSet(APIView):
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
        url = "https://www.wixapis.com/members/v1/members"

        payload = json.dumps(request.data)
        headers = {
            'Authorization': new_token['access_token'],
            'Content-Type': 'application/json',
            'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data_to_show = response.json()
        return Response(data_to_show, status=status.HTTP_201_CREATED)


class SearchAtlasRegistrationApi(APIView):

    def post(self, request):
        import requests
        import json

        url = "https://api.searchatlas.com/api/customer/account/register/v2/"

        payload = json.dumps(request.data)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return Response(response.json(), status=status.HTTP_201_CREATED)


class SearchAtlasLoginApi(APIView):
    def post(self, request):
        import requests
        import json

        url = "https://api.searchatlas.com/api/token/"

        payload = json.dumps(request.data)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return Response(response.json(), status=status.HTTP_200_OK)


class SearchAtlasCreateProjectApi(APIView):
    def post(self, request):

        try:
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

            url = "http://staff.searchenginelabs.test:8000/api/customer/projects/projects/"

            payload = json.dumps(request.data)
            headers = {
                'Authorization': new_token['access_token'],
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            return Response(response.json(), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": e.__doc__})


class WixAccountLevelSiteProperties(APIView):
    def post(self, request):
        import requests
        import json

        url = "https://www.wixapis.com/site-list/v2/sites/query"

        payload = json.dumps(request.data)
        headers = {
            'Authorization': request.headers['Authorization'],
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'wix-account-id': request.headers['Wix-Account-Id'],
            'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return Response(response.json(), status=status.HTTP_201_CREATED)


class CreateCustomerLogin(APIView):

    def post(self, request):
        import requests
        import json
        """
            API https://api.searchatlas.com/api/token/ is used to get token from server which is further used to
            authenticate and create Customer Project
        """
        url = "https://api.searchatlas.com/api/token/"

        serializer = CreateCustomerLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            header = {
                'Content-Type': 'application/json'
            }

            customer_response = requests.request("POST", url, headers=header, data=json.dumps(serializer.data))
            """
                API https://www.wixapis.com/site-list/v2/sites/query uses valid Authorization key and wix-account-id
                to get site properties. Static filter published is passed to get URL of Publish sites
            """

            url = "https://www.wixapis.com/site-list/v2/sites/query"

            payload = json.dumps(
                {
                    "query": {
                        "filter": {"published": "true"}
                    }
                }
            )
            headers = {
                'Authorization': request.data.get('Authorization'),
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'wix-account-id': request.data.get('wix_account_id'),
                'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            site_url = response.json()['sites'][0]['viewUrl']
            """
              https://api.searchatlas.com/api/customer/projects/projects/ API uses Site URL to create project for user,
              Fields domain_url, competitors and keywords are used to create Project for user
            """
            url = "https://api.searchatlas.com/api/customer/projects/projects/"

            payload = json.dumps(
                {
                    "domain_url": site_url,
                }
            )
            headers = {
                'Authorization': "Bearer" + " " + customer_response.json()['token'],
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }

            final_response = requests.request("POST", url, headers=headers, data=payload)

            return Response(final_response.json(), status=status.HTTP_201_CREATED)


class RegisterWithMember(APIView):
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
        id = request.data.get('id')
        if 'id' not in request.data:
            return Response(data={"error": "Please provide account id first"})
        url = f"https://www.wixapis.com/members/v1/members/{id}?fieldSet=FULL"

        payload = {}
        headers = {
            'Authorization': new_token['access_token'],
            'Cookie': 'XSRF-TOKEN=1672745828|QSXZP57sbvpN'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        member_data = response.json()
        url = "https://api.searchatlas.com/api/customer/account/register/v2/"

        payload = json.dumps(
            {
                "contact_name": member_data['member']['contact']['firstName'],
                "phone_number": member_data['member']['contact']['phones'][0],
                "email": member_data['member']['loginEmail'],
                "password": member_data['member']['loginEmail'].split('@')[0],
                "registration_source": "dashboard_main"
            }
        )
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        registration_response = response.json()
        return Response(registration_response)
