from exercises import is_real_palindrome, running_total, swap, \
    word_sizes, union, first_recurring, show_multiplicative_average, multiply_list, \
    sequence, word_cap, process_release_data, octal_to_decimal, anagram, \
    triangle, friday_the_13ths
import unittest

class TestIsRealPalindrome(unittest.TestCase):
    print("Testing for real palindromes...")

    def test_all_lower_case_one_word_palindrome(self):
        self.assertEquals(is_real_palindrome("madam"), True)
    
    def test_upper_case_first_letter_one_word(self):
        self.assertEquals(is_real_palindrome("Madam"), True)

    def test_sentence_with_punctuation_and_whitespace(self):
        self.assertEquals(is_real_palindrome("Madam, I'm Adam"), True)

    def test_number_as_string(self):
        self.assertEquals(is_real_palindrome("356653"), True)

    def test_all_lower_case_one_word_not_palindrome(self):
        self.assertEquals(is_real_palindrome("tommy", False)

if __name__ == "__main__":
    unittest.main()