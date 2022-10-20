class PowerSet:

    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def put(self, value):
        if self.get(value):
            return
        if self.size() == 0 or self.storage[self.size() - 1] < value:
            self.storage.append(value)
            return
        if value < self.storage[0]:
            self.storage.insert(0, value)
            return
        
        left, right = 0, self.size() - 1
        mid = self.size() // 2
        while True:
            if value < self.storage[mid]:
                right = mid
            if self.storage[mid] < value:
                left = mid
            if (right - left) == 1:
                self.storage.insert(right, value)
                return
            mid = (left + right) // 2

    def index_value(self, value):
        left, right = 0, self.size() - 1
        while left <= right:
            mid = (left + right) // 2

            if value == self.storage[mid]:
                return mid
            if value < self.storage[mid]:
                right = mid - 1
            if value > self.storage[mid]:
                left = mid + 1
        return None

    def get(self, value):
        return self.index_value(value) is not None

    def remove(self, value):
        index_value = self.index_value(value)

        if index_value is None:
            return False
        self.storage.pop(index_value)
        return True

    def intersection(self, set2):
        result_set = PowerSet()
        for value in self.storage:
            if set2.get(value):
                result_set.put(value)
        return result_set

    def union(self, set2):
        result_set = PowerSet()
        for value in self.storage:
            result_set.put(value)
        for value in set2.storage:
            result_set.put(value)
        return result_set

    def difference(self, set2):
        result_set = PowerSet()
        for value in self.storage:
            if not set2.get(value):
                result_set.put(value)
        return result_set

    def issubset(self, set2):
        for value in set2.storage:
            if not self.get(value):
                return False
        return True
