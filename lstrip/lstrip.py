def lstrip(iterable, to_strip):
    """Strip from the left of the iterable until to_strip is not met."""
    if callable(to_strip):
        should_strip = to_strip
    else:
        should_strip = lambda x: x == to_strip

    let_flow = False
    for item in iterable:
        if not should_strip(item):
            let_flow = True
        if let_flow:
            yield item
