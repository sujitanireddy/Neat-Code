#Building Hashmap from scratch in python

class HashMap:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)
    
    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        if self.current_load() < 0.05:
            return
        old_hashmap = self.hashmap
        self.hashmap = [None] * (len(old_hashmap) * 10)
        for kvp in old_hashmap:
            if kvp is not None:
                index = self.key_to_index(kvp[0])
                self.hashmap[index] = (kvp[0], kvp[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        filled_slots = 0
        for slot in self.hashmap:
            if slot is not None:
                filled_slots += 1
        return filled_slots / len(self.hashmap)

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

