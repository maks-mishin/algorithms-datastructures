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
        try:
            return self.slots.index(value)
        except ValueError:
            return None


table = HashTable(9, 3)
table.slots[0] = "a"
table.slots[2] = "a"
table.slots[3] = "a"
table.slots[4] = "a"
table.slots[5] = "a"
table.slots[6] = "a"
table.slots[7] = "a"
table.slots[8] = "a"
print(table.seek_slot("b"))
