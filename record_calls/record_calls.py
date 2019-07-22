from collections import namedtuple
import functools

NO_RETURN = object()
call = namedtuple('Call', ['args', 'kwargs', 'return_value', 'exception'])


def record_calls(inner):
    @functools.wraps(inner)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        try:
            res = inner(*args, **kwargs)
        except Exception as e:
            wrapper.calls.append(call(args, kwargs, NO_RETURN, e))
            raise(e)
        wrapper.calls.append(call(args, kwargs, res, None))

        return res

    wrapper.call_count = 0
    wrapper.calls = []

    return wrapper
