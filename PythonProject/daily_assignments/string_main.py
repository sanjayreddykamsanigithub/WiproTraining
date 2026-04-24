from string_utils.string_operations import reverse_string, to_uppercase, string_length
from string_utils.string_operations import reverse_string, to_uppercase, string_length
from string_utils.string_validations import is_palindrome, is_alphabetic

text = "madam"

print("Reversed:", reverse_string(text))
print("Uppercase:", to_uppercase(text))
print("Length:", string_length(text))

print("Is Palindrome:", is_palindrome(text))
print("Is Alphabetic:", is_alphabetic(text))