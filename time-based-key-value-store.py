#Question -> https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150

import collections

class TimeMap:

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
            
            
                

        


    






timemap = TimeMap()
#timemap.set(key="alice", value="happy", timestamp=1)
timemap.set(key="alice", value="happy", timestamp=1)
timemap.set(key="alice", value="sad", timestamp=3)
timemap.set(key="alice", value="mad", timestamp=4)
timemap.set(key="alice", value="tired", timestamp=5)
timemap.set(key="alice", value="super happy", timestamp=6)
timemap.set(key="alice", value="very sad", timestamp=7)

get_result = timemap.get(key="alice", timestamp=100)
print(get_result)
