def window(seq, size, *, fillvalue=None):
    if size == 0:
        return []

    buffer = []
    yielded = False
    count = 0

    for item in seq:
        buffer.append(item)
        buffer = buffer[-size:]
        count += 1
        if size <= count:
            yielded = True
            yield tuple(buffer)

    if not yielded:
        buffer = buffer + ([fillvalue] * (size - count))
        yield tuple(buffer)
