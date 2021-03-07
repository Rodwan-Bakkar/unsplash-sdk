# unsplash-sdk

unsplash-sdk is a command line tool to interact with the unsplash api, including GET and POST requests.

First you should create a developer account https://unsplash.com/documentation#creating-a-developer-account and get the following:
- access key
- secret key

## Authentication in unsplash api
There are two types of authentication for the api:
- Public actions, like listing photos, and for this you only need the access key to authenticate
- User specific actions, like adding a photo to a collection, for this you need OAuth authentication

### TODO:
- implement a cache functionality for the authentication class to check if the token is not yet expired so we can use it again
this helps improving performance
- implement an asynchronous downloading functionality for photos to local storage