
import os
import argparse

from unsplash_sdk.client.unsplash_client import UnsplashClient
from unsplash_sdk.client.auth import SDKAuth


API_URL = 'https://api.unsplash.com/search'


def main():

    access_key = os.environ.get('US_SDK_ACCESS_KEY')
    secret_key = os.environ.get('US_SDK_SECRET_KEY')
    email = os.environ.get('US_SDK_EMAIL')
    password = os.environ.get('US_SDK_PASSWORD')

    sdk_auth = SDKAuth(access_key, secret_key, email, password)
    uc = UnsplashClient(sdk_auth)

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, help='which method to execute')

    parser.add_argument('--download-photos', type=str, help='')

    parser.add_argument('--collection-id', type=str, help='')
    parser.add_argument('--photo-id', type=str, help='')

    args = parser.parse_args()

    action = args.action

    if action == 'list_photos':
        uc.list_photos()
    elif action == 'list_collections':
        pass
    elif action == 'create_collection':
        pass
    elif action == 'add_photo_to_collection':
        pass


if __name__ == '__main__':
    main()
