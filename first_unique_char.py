#Questin -> https://leetcode.com/problems/first-unique-character-in-a-string/description/
import collections
def first_unique_char(word: str) -> str:

    hashmap = collections.defaultdict(int)

    for letter in word:
        hashmap[letter] = hashmap[letter] + 1
    
    for key in hashmap.keys():
        if hashmap[key] == 1:
            return key

print(first_unique_char(""))