#Question -> https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150

import collections

#Bute Force: Time Complexity: O(n) and Space Complexity: O(n)
class TimeMap_Brute:

    def __init__(self):
        self.keystore = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keystore:
            return ""
    
        else:
            seen = 0
            seen_value = ''
            for value_time in self.keystore[key]:
                if value_time[1] <= timestamp:
                    seen = max(seen, value_time[1])
                    seen_value = value_time[0]
        return seen_value
            
#Optimal Way: Time Complexity: O(log n) and Space Complexity: O(n)
class TimeMap:

    def __init__(self):
        self.keystore = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keystore:
            return ""
    
        else:
            arr = self.keystore[key]
            l = 0
            r = len(arr) - 1
            result = ""

            while l <= r:

                mid = (l+r) // 2
                
                if arr[mid][1] <= timestamp:
                    result = arr[mid][0]
                    l = mid + 1
                
                else:
                    r = mid - 1
            
            return result
            
                

        


    





#testing
timemap = TimeMap()

timemap.set(key="alice", value="happy", timestamp=1)
timemap.set(key="alice", value="sad", timestamp=3)
timemap.set(key="alice", value="mad", timestamp=4)
timemap.set(key="alice", value="tired", timestamp=5)
timemap.set(key="alice", value="super happy", timestamp=6)
timemap.set(key="alice", value="very sad", timestamp=7)


get_result = timemap.get(key="alice", timestamp=100)
print(get_result)
