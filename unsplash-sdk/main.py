
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
    # uc.list_photos(True)
    # uc.list_collections()
    uc.create_collection('test_collection2')


if __name__ == '__main__':
    main()

