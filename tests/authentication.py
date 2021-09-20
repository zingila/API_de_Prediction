import requests
from requests.auth import HTTPBasicAuth
from utils import test, API_URL, USERNAME


class AuthenticationException(Exception):
    pass


@test
def invalid_authentication():

    res = requests.post(
        f"{API_URL}/prediction", auth=HTTPBasicAuth(USERNAME, "INVALID_PASSWORD")
    )

    if res.status_code != 401:
        raise AuthenticationException(
            f"Expected status is 401 but actual status is : {res.status_code}"
        )

    return True
