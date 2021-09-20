import requests
import os
from requests.auth import HTTPBasicAuth
from utils import test, API_URL, USERNAME, PASSWORD


class ContentException(Exception):
    pass


DATA = {
    "gender": "Male",
    "age": 0,
    "hypertension": True,
    "heart_disease": True,
    "ever_married": "Yes",
    "work_type": "children",
    "Residence_type": "Rural",
    "avg_glucose_level": 0,
    "bmi": 0,
    "smoking_status": "Unknown",
}


@test
def valid_body():

    res = requests.post(
        f"{API_URL}/prediction", auth=HTTPBasicAuth(USERNAME, PASSWORD), json=DATA
    )

    if res.status_code != 200:
        raise ContentException(
            f"Expected status is 200 but actual status is : {res.status_code}"
        )

    return True


@test
def invalid_body():

    res = requests.post(
        f"{API_URL}/prediction",
        auth=HTTPBasicAuth(USERNAME, PASSWORD),
        json={"invalid_data": True},
    )

    if res.status_code != 422:
        raise ContentException(
            f"Expected status is 422 but actual status is : {res.status_code}"
        )

    return True
