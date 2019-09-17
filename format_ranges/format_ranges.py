def format_ranges(input):
    seq = list(input)
    ranges = ""
    while len(seq) > 0:
        seq, next_range = peel_lowest_range(seq)
        if len(ranges) == 0:
            ranges = next_range
        else:
            ranges += "," + next_range

    return ranges


def peel_lowest_range(seq):
    low = min(seq)
    hi = low
    seq.pop(seq.index(low))
    while True:
        if len(seq) == 0:
            break
        next = min(seq)
        if next == hi + 1:
            hi = next
            seq.pop(seq.index(hi))
        else:
            break

    if low == hi:
        return seq, f"{low}"
    else:
        return seq, f"{low}-{hi}"
