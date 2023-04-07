import json

import requests
from django.conf import settings


class WixAuthentication:

    def get_wix_authentication(self, refresh_token):
        url = "https://www.wixapis.com/oauth/access"

        payload = json.dumps({
            "grant_type": "authorization_code" if not refresh_token else 'refresh_token',
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "refresh_token" if refresh_token else "code": refresh_token if refresh_token else self.request.data.get('token')
        })
        headers = {
            'Authorization': "",
            'Content-Type': 'application/json',
            'Cookie': 'XSRF-TOKEN=1674905988|UeW4vyx1AKMr'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response

