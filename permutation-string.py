#Question -> https://neetcode.io/problems/permutation-string/question?list=neetcode150

import collections


#time complexity = O(n)
#space complexity = O(1)
def checkInclusion(s1: str, s2: str) -> bool:

    if len(s1) > len(s2):
        return False

    #freq hashmap for s1
    freq_hashmap_s1 = collections.defaultdict(int)
    for char in s1:
        freq_hashmap_s1[char] += 1
    
    L = 0
    window_size = len(s1)
    freq_hashmap_s2 = collections.defaultdict(int)

    for R in range(len(s2)):
        freq_hashmap_s2[s2[R]] += 1

        if freq_hashmap_s2 == freq_hashmap_s1:
            return True
        
        if (R - L + 1) == window_size:

            freq_hashmap_s2[s2[L]] -= 1

            if freq_hashmap_s2[s2[L]] == 0:
                del freq_hashmap_s2[s2[L]]
            
            L += 1
    
    return False