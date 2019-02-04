def parse_ranges(ranges):
    """Return all values within the `ranges` requested, as such: "1-2,4-4,8-10"."""
    for item in ranges.split(","):
        bounds = item.split("-")
        start = int(bounds[0])
        try:
            end = int(bounds[1])
        except (IndexError, ValueError):
            end = start
        for val in range(start, end + 1):
            yield val
