from datetime import datetime


def time_to(target, timeformat="%Y-%m-%d %H:%M:%S"):
    """
    Get number of seconds to target time.
    """
    return (datetime.strptime(target, timeformat) - datetime.now()).total_seconds()

