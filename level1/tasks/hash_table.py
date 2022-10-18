class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        total_size, salt = 0, 1.618
        for ch in value:
            total_size += ord(ch) * salt
        return int(total_size) % self.size

    def seek_slot(self, value):
        index_slot = self.hash_fun(value)
        step = self.step
        if self.size % step == 0:
            step += 1
        count_steps = 0
        while self.slots[index_slot] is not None:
            index_slot = (index_slot + step) % self.size
            count_steps += 1
            if count_steps > self.size:
                return None
        return index_slot

    def put(self, value):
        index_slot = self.seek_slot(value)
        if index_slot is not None:
            self.slots[index_slot] = value
            return index_slot
        return None

    def find(self, value):
        for index_slot in range(self.size):
            if self.slots[index_slot] != value:
                continue
            return index_slot
        return None
