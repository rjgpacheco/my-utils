import random, string

ALPHANUMERIC = string.ascii_uppercase + string.ascii_lowercase + string.digits


def random_alphanumeric(n):
    """Return a random alphanumeric string of size n"""
    return "".join(random.choice(ALPHANUMERIC) for _ in range(n))
