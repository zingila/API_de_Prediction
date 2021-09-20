from authentication import invalid_authentication
from content import valid_body, invalid_body
import time


def make_tests():

    invalid_authentication()
    valid_body()
    invalid_body()


if __name__ == "__main__":
    # Sleep 2 seconds to make sure the API is up and running.
    # We could use tools like https://github.com/vishnubob/wait-for-it
    # instead (see https://docs.docker.com/compose/startup-order/).
    # But for now this is enough.
    time.sleep(2)
    make_tests()
