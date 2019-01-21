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


class WeekdayEnum:
    def __init__(self):
        self.MONDAY = 0
        self.TUESDAY = 1
        self.WEDNESDAY = 2
        self.THURSDAY = 3
        self.FRIDAY = 4
        self.SATURDAY = 5
        self.SUNDAY = 6


Weekday = WeekdayEnum()
