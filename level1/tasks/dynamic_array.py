import ctypes


class DynArray:
    """Dynamic array class (similar to Python list)"""

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.min_capacity = 16
        self.array = self.make_array(self.capacity)

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __len__(self):
        return self.count

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = item
        self.count += 1

    def insert(self, i, item):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        if i == self.count:
            self.append(item)
            return
        self._increase_capacity()

        for pos in range(self.count - 1, i - 1, -1):
            self.array[pos + 1] = self.array[pos]
        self.array[i] = item
        self.count += 1

    def _increase_capacity(self):
        if self.count + 1 > self.capacity:
            self.resize(2 * self.capacity)

    def print(self):
        for i in range(self.count):
            print(self.array[i], end=' ')

    def _shrink_capacity(self):
        if self.count / self.min_capacity < 0.5:
            self.capacity = self.min_capacity
            return
        if (self.count / self.capacity < 0.5 and
                int(self.capacity / 1.5) >= self.min_capacity):
            self.capacity = int(self.capacity / 1.5)

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for pos in range(i, self.count - 1):
            self.array[pos] = self.array[pos + 1]
        self.array[self.count - 1] = None
        self.count -= 1
        self._shrink_capacity()
