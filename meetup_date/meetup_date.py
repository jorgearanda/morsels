from calendar import Calendar
from collections import defaultdict
from datetime import date
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    """Return the date when a monthly meetup should take place."""
    dates_by_weekday = _get_dates_by_weekday(year, month)
    if 0 < nth:
        nth -= 1

    return dates_by_weekday[weekday][nth]


def _get_dates_by_weekday(year, month):
    """Return a dict with weekdays as keys and sorted days in the month as values."""
    cal = Calendar()
    dates_by_weekday = defaultdict(list)
    for day_of_month, weekday in cal.itermonthdays2(year, month):
        if day_of_month == 0:
            continue
        dates_by_weekday[weekday].append(date(year, month, day_of_month))

    return dates_by_weekday
