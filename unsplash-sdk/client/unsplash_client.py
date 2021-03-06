import json
import requests
import urllib


class UnsplashClient:
    API_URL = 'https://api.unsplash.com'
    PHOTOS_URL = '{}/photos'.format(API_URL)
    COLLECTIONS_URL = '{}/collections'.format(API_URL)

    def __init__(self, sdk_auth):
        self.sdk_auth = sdk_auth

    @staticmethod
    def download_images(results_list):
        local_storage_path = 'local_storage'
        for image_info in results_list[0:1]:
            image_id = image_info['id']
            image_url = image_info['urls']['thumb']
            image_storage_path = '{}/{}.jpg'.format(local_storage_path, image_id)
            urllib.request.urlretrieve(image_url, image_storage_path)
            print('image downloaded to local storage')

    def list_photos(self, download_results=False):
        auth_headers = self.sdk_auth.get_auth_headers(action_type='public')
        try:
            response = requests.get(url=self.PHOTOS_URL, headers=auth_headers)
            response_body = json.loads(response.content)
            if download_results:
                self.download_images(response_body)

        except Exception as e:
            print(e)

    def list_collections(self):
        auth_headers = self.sdk_auth.get_auth_headers(action_type='public')
        try:
            response = requests.get(url=self.COLLECTIONS_URL, headers=auth_headers)
            response_body = json.loads(response.content)

            print(len(response_body))

        except Exception as e:
            print(e)

    def create_collection(self, title, description=None, private=False):
        auth_headers = self.sdk_auth.get_auth_headers(action_type='user-specific')
        post_data = {
            'title': title,
            'private': private,
        }
        if description:
            post_data['description'] = description

        try:
            response = requests.post(url=self.COLLECTIONS_URL, data=post_data, headers=auth_headers)
            response_body = json.loads(response.content)

            print('Collection, {}, was created'.format(response_body.get('title')))

        except Exception as e:
            print(e)

    def add_photo(self):
        pass

