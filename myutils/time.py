from datetime import datetime, timedelta
from time import sleep

from dateutil import parser


def parse_time(str, format=None) -> datetime:
    if isinstance(str, datetime):
        return str
    elif format is None:
        return parser.parse(str)
    else:
        return datetime.strptime(str, format)


def time_to(target):
    """
    Get number of seconds to target time.
    """
    return (parse_time(str, format) - datetime.now()).total_seconds()


def sleep_until(target, silent=False):
    target = parse_time(str, format)
    remaining = time_to(parse_time(str, format))
    if remaining <= 0:
        if not silent:
            print("Specified time already passed.")
    else:
        if not silent:
            print(f"Sleeping for {remaining} seconds, until {target}")
        sleep(remaining)


def time_range(start, stop, delta: timedelta, include_start=True, include_stop=True):
    def gen_time_range(start, stop, delta, include_start, include_stop):
        t = start if include_start else start + delta
        while True:
            if (include_stop and t > stop) or (not include_stop and t == stop):
                return
            yield t
            t = t + delta

    start = parse_time(start)
    stop = parse_time(stop)

    if start >= stop:
        raise ValueError(f"'start' ({start=}) is after of equal to 'stop' ({stop=}) .")

    return gen_time_range(start, stop, delta, include_start, include_stop)

