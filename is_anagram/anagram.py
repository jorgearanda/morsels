import unicodedata


def is_anagram(first_string, second_string):
    return sorted_letters(first_string) == sorted_letters(second_string)


def sorted_letters(string):
    ascii_string = (
        unicodedata.normalize("NFKD", string).encode("ASCII", "ignore").decode("utf-8")
    )

    return sorted([letter for letter in ascii_string.lower() if letter.isalpha()])
