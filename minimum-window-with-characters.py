#Question -> https://neetcode.io/problems/minimum-window-with-characters/question?list=neetcode150


#Time Complexity: O(n)
#Space Complexity: O(n)

import collections
def minWindow(s: str, t: str) -> str:

    t_map = collections.defaultdict(int)

    for char in t:
        t_map[char] += 1

    s_map = collections.defaultdict(int)

    L = 0
    
    have, need = 0, len(t_map)

    best_window = ""
    
    for R in range(len(s)):

        s_map[s[R]] += 1

        if s[R] in t_map and s_map[s[R]] == t_map[s[R]]:
            have += 1
        
        while have == need:

            current_window = s[L:R+1]

            if best_window == "" or len(current_window) < len(best_window):

                best_window = current_window

            #manage L pointer 
            s_map[s[L]] -= 1

            if s[L] in t_map and s_map[s[L]] < t_map[t[L]]:

                have -= 1
            
            L += 1
        
    return best_window




        













print(minWindow(s = "OUZODYXAZV", t = "XYZ"))