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