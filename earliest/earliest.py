def get_earliest(*dates):
    return min(dates, key=date_key)


def date_key(date):
    (m, d, y) = date.split('/')
    return (y, m, d)
