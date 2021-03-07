
import argparse

from client.unsplash_client import UnsplashClient
from client.auth import SDKAuth


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--access_key', type=str, help='unsplash api access key for developer account')
    parser.add_argument('--secret_key', type=str, help='unsplash api secret key for developer account')
    parser.add_argument('--email', type=str, help='email for developer account')
    parser.add_argument('--password', type=str, help='password for developer account')

    args = parser.parse_args()
    access_key = args.access_key
    secret_key = args.secret_key
    email = args.email
    password = args.password

    sdk_auth = SDKAuth(access_key, secret_key, email, password)
    uc = UnsplashClient(sdk_auth)

    actions = ['list_photos', 'list_collection', 'create_collection', 'add_photo_to_collection']
    action = actions[0]

    if action == 'list_photos':
        uc.list_photos(20, False)
    elif action == 'list_collection':
        uc.list_collections()
    elif action == 'create_collection':
        uc.create_collection('test_collection23', 'some_description', True)
    elif action == 'add_photo_to_collection':
        uc.add_photo_to_collection('23640519', 'KIDGf43UPOw')


if __name__ == '__main__':
    main()

