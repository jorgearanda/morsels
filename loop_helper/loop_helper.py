from dataclasses import dataclass


def loop_helper(seq, previous_default=None):
    info = Info(
        index=0,
        is_first=True,
        is_last=False,
        previous=None,
        current=previous_default,
        next=None,
    )
    initializing = True
    for item in seq:
        if initializing:
            info.next = item
            initializing = False
            continue
        info.previous, info.current, info.next = info.current, info.next, item
        yield info.current, info
        info.index += 1
        info.is_first = False
    else:
        if not initializing:
            info.previous, info.current, info.next = info.current, info.next, None
            info.is_last = True
            yield info.current, info


@dataclass
class Info:
    index: int
    is_first: bool
    is_last: bool
    previous: any
    current: any
    next: any
