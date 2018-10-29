def get_earliest(*dates):
    earliest = dates[0]
    for date in dates:
        if to_ymd(date) < to_ymd(earliest):
            earliest = date

    return earliest


def to_ymd(date):
    """Assume input is in format MM/DD/YYYY. Return formatted as YYYYMMDD."""
    return date[-4:] + date[:2] + date[3:5]
