from exercises import is_real_palindrome, running_total, swap, \
    word_sizes, union, first_recurring, show_multiplicative_average, multiply_list, \
    sequence, word_cap, process_release_data, octal_to_decimal, anagram, \
    triangle, friday_the_13ths
import unittest

class TestIsRealPalindrome(unittest.TestCase):
    print("Testing for real palindromes...")

    def test_all_lower_case_one_word(self):
        self.assertTrue(is_real_palindrome("madam"))
    
    def test_upper_case_first_letter_one_word(self):
        self.assertTrue(is_real_palindrome("Madam"))

    def test_sentence_with_multiple_upper_case(self):
        self.assertTrue(is_real_palindrome("Madam, I'm Adam"))

    def test_number_as_string(self):
        self.assertTrue(is_real_palindrome("356653"))

    def test_sentence_with_punctuation_at_end(self):
        self.assertTrue(is_real_palindrome("Eva, can I see bees in a cave?"))
    
    def test_sentence_with_punctuation_in_middle(self):
        self.assertTrue(is_real_palindrome("No lemon, no melon"))

    def test_mixed_alphanumeric(self):
        self.assertTrue(is_real_palindrome("356a653"))



class TestIsNotRealPalindrome(unittest.TestCase):
    print("Testing for false palindromes...")

    def test_all_lower_case_one_word(self):
        self.assertFalse(is_real_palindrome("tommy"))

    def test_mixed_alphanumeric(self):
        self.assertFalse(is_real_palindrome("123ab321"))


if __name__ == "__main__":
    unittest.main()