from datetime import datetime


def time_to(target, format="%Y-%m-%d %H:%M:%S"):
    """
    Get number of seconds to target time.
    """
    return datetime.strptime(target, format=format) - datetime.now().total_seconds()

    