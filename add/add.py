from itertools import zip_longest


def add(*matrices):
    try:
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e
