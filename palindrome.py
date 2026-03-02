#Question -> https://neetcode.io/problems/is-palindrome/question?list=neetcode150

#Valid Palindrome - Two pointer algorithm
def is_palindrome(word):

    L, R = 0, len(word) - 1

    while L < R:

        while L < R and not word[L].isalnum():
            L += 1
        
        while L < R and not word[R].isalnum():
            R -= 1

        if word[L].lower() == word[R].lower():
            
            L += 1
            R -= 1
        
        else:
            return False
    
    return True

print(is_palindrome(word="Was it a car or a cat I saw?"))


#Valid Palindrome the regular way. Can also use list slicing[::-1] to reverse a string.
def isPalindrome_On(self, s: str) -> bool:

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