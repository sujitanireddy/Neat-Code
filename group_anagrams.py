#Question - https://neetcode.io/problems/anagram-groups/question?list=neetcode150


#Brute Force - My first intution
#Time Complexity: O(N * KlogK)
def groupAnagrams(strs: list[str]) -> list[list[str]]:

    hashmap = {}
    
    #Build a dict with sorted word as key and an empty list
    for word in strs: 
        hashmap[''.join(sorted(word))] = []
    
    #For each word if it's sorted version is a key then append the word to the value list
    for word in strs:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)

    return list(hashmap.values())


#Learned about default dict - https://docs.python.org/3/library/collections.html#collections.defaultdict
#One loop can be avoided to build the hashmap.
#Time Complexity: O(m * nlogn)

from collections import defaultdict

def groupAnagrams_defaultdict(strs: list[str]) -> list[list[str]]:

    #defaultdict will take care of keyErrors
    hashmap = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        hashmap[sorted_word].append(word)

    return list(hashmap.values())