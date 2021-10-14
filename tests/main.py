from authentication import invalid_authentication
from content import valid_body, invalid_body
import time


def make_tests():

    invalid_authentication()
    valid_body()
    invalid_body()


if __name__ == "__main__":
    # 2 secondes de pause pour vous assurer que l'API est opérationnelle.
    # Nous pourrions utiliser des outils comme (voir https://docs.docker.com/compose/startup-order/).
    # Mais pour l'instant c'est suffisant.
    time.sleep(2)
    make_tests()
