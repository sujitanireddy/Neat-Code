#Valid Palindrome - Two pointer algorithm
def is_palindrome(word):

    L, R = 0, len(word) - 1

    while L < R:

        if word[L] == word[R]:
            
            L += 1
            R -= 1
        
        else:
            return False
    
    return True

print(is_palindrome(word=""))


#Valid Palindrome the regular way. Can also use list slicing[::-1] to reverse a string.
def isPalindrome(self, s: str) -> bool:

    reversed_s = ''
    for i in range(len(s) - 1, -1 , -1):
        if s[i].isalnum():
            reversed_s += s[i]

    stripped_s = ''
    for i in range(len(s)):
        if s[i].isalnum():
            stripped_s += s[i]
        
    if stripped_s.lower() == reversed_s.lower():
        return True
    else:
        return False