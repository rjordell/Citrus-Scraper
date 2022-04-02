import requests

from oauthlib.oauth2 import WebApplicationClient
client_id = 'XXX'
client = WebApplicationClient(client_id)

authorization_url = 'https://<canvas-install-url>/login/oauth2/auth'

url = client.prepare_request_uri(
    authorization_url,
    redirect_uri = 'urn:ietf:wg:oauth:2.0:oob',
    scope = 'url:GET|/api/v1/courses/:course_id/assignment_groups',
    state = 'D8302HHUUDHH'
)
