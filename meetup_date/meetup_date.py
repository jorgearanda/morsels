from collections import defaultdict
from datetime import date, timedelta
from enum import Enum


def meetup_date(year, month, nth=4, weekday=3):
    """Return the date when a monthly meetup should take place."""
    dates_by_weekday = defaultdict(list)
    day = date(year, month, 1)
    while True:  # Easier to build the whole calendar month due to edge cases
        dates_by_weekday[day.weekday()].append(day)
        day = day + timedelta(days=1)
        if day.month != month:
            break

    if 0 < nth:
        nth -= 1

    return dates_by_weekday[weekday][nth]


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
