from datetime import datetime
from time import sleep

def time_to(target, timeformat="%Y-%m-%d %H:%M:%S"):
    """
    Get number of seconds to target time.
    """
    return (datetime.strptime(target, timeformat) - datetime.now()).total_seconds()


def sleep_until(target, timeformat="%Y-%m-%d %H:%M:%S", silent=False):
    remaining = time_to(target=target, timeformat=timeformat)
    if remaining <= 0:
        if not silent:
            print("Specified time aleady passed.")
    else:
        if not silent:
            print(f"Sleeping for {remaining} seconds, until {target}")
        sleep(remaining)


