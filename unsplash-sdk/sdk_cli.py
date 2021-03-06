
import argparse
from client.unsplash_client import UnsplashClient


def main():
    api_url = 'https://api.unsplash.com/search'

    parser = argparse.ArgumentParser()
    parser.add_argument('--access_key', type=str, help='unsplash api access key for developer account')
    parser.add_argument('--action', type=str, help='which method to execute')
    parser.add_argument('--query_subject', type=str, help='which subject to search photos for')

    args = parser.parse_args()
    access_key = args.access_key
    action = args.action
    query_subject = args.query_subject

    uc = UnsplashClient(api_url, access_key)
    if action == 'list_photos':
        uc.list_photos(query_subject)
    elif action == 'list_collections':
        pass
    elif action == 'create_collection':
        pass
    elif action == 'add_photo_to_collection':
        pass


if __name__ == '__main__':
    main()
