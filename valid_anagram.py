#Question - https://neetcode.io/problems/is-anagram/question?list=neetcode150

#Brue Force Approach using dict(hashmap)
#Time Complexity: 0(n)
def isAnagram(s: str, t: str) -> bool:
        
    s_dict = {}
    t_dict = {}

    for letter in s:
        s_dict[letter] = 1 + s_dict.get(letter, 0)
        
    for letter in t:
        t_dict[letter] = 1 + t_dict.get(letter, 0)
        
    if s_dict == t_dict:
        return True
        
    else:
        return False
    

#Using Sorted built in function.
#Time Complexity: O(nlogn). The time it takes to sort
def isAnagram_sorted(s: str, t: str) -> bool:
        
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
        return True
    return False