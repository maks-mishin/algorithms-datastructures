class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum([ord(sym) for sym in key]) % self.size
    
    def is_key(self, key):
        return key in self.slots

    def clear(self):
        min_hit = min(self.hits)
        index_slot = self.hits.index(min_hit)
        self.slots[index_slot] = None
        self.values[index_slot] = None
        self.hits[index_slot] = 0
        return index_slot
    
    def seek_slot(self, key):
        index_slot = self.hash_fun(key)
        step = 3
        if self.size % step == 0:
            step += 1
        count_steps = 0
        while self.slots[index_slot] is not None:
            index_slot = (index_slot + step) % self.size
            count_steps += 1
            if count_steps == self.size:
                return self.clear()
        return index_slot
    
    def get_key_index(self, key):
        return self.slots.index(key)

    def get(self, key):
        if self.is_key(key):
            index_slot = self.get_key_index(key)
            self.hits[index_slot] += 1
            return self.values[index_slot]
        return None

    def put(self, key, value):
        if self.is_key(key):
            self.values[self.get_key_index(key)] = value
            return
        index_slot = self.seek_slot(key)
        self.slots[index_slot] = key
        self.values[index_slot] = value
