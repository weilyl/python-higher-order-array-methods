import re

def is_real_palindrome(potential_palindrome: str) -> bool:
    """
    Checks if a string is a palindrome regardless of casing, whitespace and punctuation.

    :param input_string: STR input string of any characters
    :return: BOOL whether or not string is a palindrome
    """
    # strip whitespace and punctuation so only alphanumeric chars remain (regex?)
    # force casing (either lower or upper case; I am choosing upper case)
    potential_palindrome_alpha = re.sub('[^a-zA-Z0-9]+', '', potential_palindrome).upper()

    half_length = int(len(potential_palindrome_alpha)/2)

    reversed_first_half = potential_palindrome_alpha[:half_length][::-1]

    return potential_palindrome_alpha.endswith(reversed_first_half)


def running_total(input_arr: list) -> int:
    return NotImplemented

def swap(sentence: str) -> str:
    return NotImplemented

def word_sizes(input_sentence: str) -> dict:
    return NotImplemented

def union(arr1: list, arr2: list) -> list:
    return NotImplemented

def first_recurring(word: str) -> str: 
    return NotImplemented

def show_multiplicative_average(input: list) -> int: 
    return NotImplemented

def multiply_list(arr1: list, arr2: list) -> int:
    return NotImplemented

def sequence(num: int) -> list: 
    return NotImplemented

def word_cap(sentence: str) -> str: 
    return NotImplemented

def process_release_data(new_releases: list) -> list: 
    return NotImplemented

def octal_to_decimal(number_string: str) -> int: 
    return NotImplemented

def anagram(word: str, array: list) -> str: 
    return NotImplemented

def triangle(a: int, b: int, c: int) -> str: 
    return NotImplemented

def friday_the_13ths(year: int) -> int: 
    return NotImplemented

if __name__ == "__main__":
  is_real_palindrome("Madam__, I'm Adam")