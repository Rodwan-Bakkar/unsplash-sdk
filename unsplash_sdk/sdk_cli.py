
import os
import argparse

from unsplash_sdk.client.unsplash_client import UnsplashClient
from unsplash_sdk.client.auth import SDKAuth


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
    parser.add_argument('--per-page', type=str, help='')

    parser.add_argument('--collection-title', type=str, help='')
    parser.add_argument('--collection-description', type=str, help='')
    parser.add_argument('--collection-private', type=str, help='')

    parser.add_argument('--collection-id', type=str, help='')
    parser.add_argument('--photo-id', type=str, help='')

    args = parser.parse_args()

    action = args.action

    download_photos = args.download_photos if args.download_photos else False
    per_page = args.per_page if args.per_page else 10

    collection_title = args.collection_title
    collection_description = args.collection_description
    collection_private = args.collection_private if args.collection_private else False

    collection_id = args.collection_id
    photo_id = args.photo_id

    if action == 'list_photos':
        uc.list_photos(per_page, download_photos)
    elif action == 'list_collections':
        uc.list_collections()
    elif action == 'create_collection':
        uc.create_collection(collection_title, collection_description, collection_private)
    elif action == 'add_photo_to_collection':
        uc.add_photo_to_collection(collection_id, photo_id)


if __name__ == '__main__':
    main()
