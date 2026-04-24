def is_palindrome(s):
    return s == s[::-1]

print("madam:", is_palindrome("madam"))
print("hello:", is_palindrome("hello"))