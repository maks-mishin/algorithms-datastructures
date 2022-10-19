class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        total_size, salt = 0, 1.618
        for ch in key:
            total_size += ord(ch) * salt
        return int(total_size) % self.size

    def is_key(self, key):
        return key in self.slots

    def seek_slot(self, key):
        index_slot = self.hash_fun(key)
        step = 3
        if self.size % step == 0:
            step += 1
        count_steps = 0
        while self.slots[index_slot] is not None:
            index_slot = (index_slot + step) % self.size
            count_steps += 1
            if count_steps > self.size:
                return None
        return index_slot

    def get_key_index(self, key):
        return self.slots.index(key)

    def put(self, key, value):
        if self.is_key(key):
            self.values[self.get_key_index(key)] = value
            return
        index_slot = self.seek_slot(key)
        self.slots[index_slot] = key
        self.values[index_slot] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[self.get_key_index(key)]
        return None
