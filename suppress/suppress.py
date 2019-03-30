from contextlib import contextmanager


class ExceptionInfo:
    exception = None
    traceback = None


@contextmanager
def suppress(*exception_types):
    exception_info = ExceptionInfo()
    try:
        yield exception_info
    except exception_types as e:
        exception_info.exception = e
        exception_info.traceback = e.__traceback__
