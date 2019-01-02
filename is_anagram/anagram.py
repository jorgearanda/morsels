import unicodedata


def is_anagram(first_string, second_string):
    return sorted_letters(first_string) == sorted_letters(second_string)


def sorted_letters(string):
    string = unicodedata.normalize("NFKD", string).lower()

    return sorted([letter for letter in string if letter.isalpha()])
