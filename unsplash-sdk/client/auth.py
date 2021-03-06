
from requests_oauthlib.oauth2_session import OAuth2Session
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SDKAuth:
    API_URL = "https://unsplash.com"
    AUTH_URL = "{}/oauth/authorize".format(API_URL)
    TOKEN_URL = "{}/oauth/token".format(API_URL)
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    def __init__(self, access_key, secret_key, email, password):

        self.access_key = access_key
        self.secret_key = secret_key
        self.email = email
        self.password = password

    def get_auth_headers(self, action_type):
        if action_type == 'public':
            headers = {
                'Authorization': 'Client-ID {}'.format(self.access_key)
            }
        elif action_type == 'user-specific':

            oauth = OAuth2Session(client_id=self.access_key,
                                  redirect_uri=self.REDIRECT_URI,
                                  scope=['write_collections'])
            authorization_url, state = oauth.authorization_url(self.AUTH_URL,
                                                               access_type="offline",
                                                               grant_type='authorization_code'
                                                               )

            options = webdriver.ChromeOptions()
            options.add_argument("headless")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

            driver.implicitly_wait(10)
            try:
                driver.get(authorization_url)
                email_input = driver.find_element_by_xpath('//input[@id="user_email"]')
                email_input.send_keys(self.email)
                password_input = driver.find_element_by_xpath('//input[@id="user_password"]')
                password_input.send_keys(self.password)
                driver.find_element_by_xpath('//input[@type="submit"]').click()
                code = driver.find_element_by_tag_name('code').text
            finally:
                driver.quit()

            token = oauth.fetch_token(
                token_url=self.TOKEN_URL,
                client_secret=self.secret_key,
                code=code
            )

            headers = {
                'Authorization': 'Bearer {}'.format(token.get('access_token'))
            }

        return headers




