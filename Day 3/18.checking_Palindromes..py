


def is_palindrome(s):
    list_s = list(s)
    reversed_s = list_s
    reversed_s.reverse()
    return list_s == reversed_s

print(is_palindrome("milk"))



def  is_palindrome(s):
    reversed_string = "".join(reversed(s))
    return reversed(s) == s

print (is_palindrome("kayak"))


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("kmilkk"))