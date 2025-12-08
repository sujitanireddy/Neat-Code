#Question - https://neetcode.io/problems/is-anagram/question?list=neetcode150

#Brue Force Approach using dict(hashmap)
#Time Complexity: 0(n)
def isAnagram(s: str, t: str) -> bool:
    
    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
    return s_dict == t_dict

#Using Sorted built in function.
#Time Complexity: O(nlogn). The time it takes to sort
def isAnagram_sorted(s: str, t: str) -> bool:
        
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
        return True
    return False