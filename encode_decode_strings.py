#Question - https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

class Solution:

    def encode(self, strs: list[str]) -> str:

        #for the sake of simplicity using '#' as the dilimiter.
        delimiter = '#'
        encoded_string = ''

        for word in strs:
            word_length = len(word)
            encoded_string += f'{word_length}{delimiter}{word}'
        
        return encoded_string

    def decode(self, s: str) -> list[str]:

        delimiter = '#'
        decoded_list = []
        i = 0

        #loop to traverse from start of the encoded string to the end
        while i < len(s):

            #the idea is to capture the length. The number can be of varied digits, so we need another loop to capture it.
            #j is going to be the index of that inner loop
            j = i
            
            #until the pointer points to the delimiter, keep capturing the length. 
            while s[j] != delimiter:
                j+=1
            
            word_length = int(s[i:j])

            start_of_the_word = j+1
            end_of_the_word = start_of_the_word + word_length
            decoded_list.append(s[start_of_the_word:end_of_the_word])

            i = end_of_the_word
        
        return decoded_list
    



"""
Notes:

- "For loop" already has a defined iterator. Modifying "i" within the loop does not affect the iterator. If you want to jump, while loop is the goto option.
    
Example:

    for i in range(5):
    print(f"Start of iteration: i = {i}")
    i = 100  # This gets ignored!
    print(f"After manual change: i = {i}")

- "i" should not be incremented to "the end_of_the_word + 1". Because end_of_the_word is already pointing to the start of the word.

"""