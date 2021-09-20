import os


def test(func):
    def wrapper():
        print(f"Testing function : {func.__name__}.")
        res = func()
        if res:
            print(f"Passed.")
    return wrapper

API_URL = os.getenv("API_URL", "http://localhost:8000")
USERNAME = "Daniel"
PASSWORD = "secretpassword"