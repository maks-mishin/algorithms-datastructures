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
        if None not in self.slots:
            return None

        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index

        # using linear probing
        current_index = index
        while self.slots[current_index] is not None:
            current_index += self.step
            if current_index > self.size - 1:
                current_index = current_index % self.size
        return current_index

    def put(self, value):
        index_slot = self.hash_fun(value)
        if index_slot is not None:
            self.slots[index_slot] = value
            return index_slot

        index_slot = self.seek_slot(value)
        if index_slot is not None:
            self.slots[index_slot] = value
            return index_slot
        return None

    def find(self, value):
        try:
            return self.slots.index(value)
        except ValueError:
            return None
