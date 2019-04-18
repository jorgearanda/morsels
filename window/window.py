def window(seq, length):
    buffer = []
    for item in seq:
        buffer.append(item)
        buffer = buffer[-length:]
        if len(buffer) == length:
            yield tuple(buffer)
