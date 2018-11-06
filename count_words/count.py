import string

punctuation = string.punctuation + '¡¿'


def count_words(input):
    freq = {}
    for word in input.split():
        token = word.lower().strip(punctuation)
        freq[token] = freq.get(token, 0) + 1

    return freq
