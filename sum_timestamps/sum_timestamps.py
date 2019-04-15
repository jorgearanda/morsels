from datetime import datetime


def sum_timestamps(input):
    return _to_timestamp(sum(map(_get_seconds, input)))


def _get_seconds(timestamp):
    try:
        dt = datetime.strptime(timestamp, '%H:%M:%S')
    except ValueError:
        dt = datetime.strptime(timestamp, '%M:%S')

    return dt.hour * 3600 + dt.minute * 60 + dt.second


def _to_timestamp(seconds):
    hours_str = _get_hours_str(seconds)
    minutes_str = _get_minutes_str(seconds)
    seconds_str = _get_seconds_str(seconds)
    return hours_str + minutes_str + seconds_str


def _get_hours_str(seconds):
    if 3600 <= seconds:
        return str(seconds // 3600) + ':'
    else:
        return ''


def _get_minutes_str(seconds):
    if 3600 <= seconds:
        return str((seconds % 3600) // 60).zfill(2) + ':'
    else:
        return str(seconds // 60) + ':'


def _get_seconds_str(seconds):
    return str(seconds % 60).zfill(2)
