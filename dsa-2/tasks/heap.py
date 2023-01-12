from typing import List, Union


class Heap:

    def __init__(self):
        self.HeapArray: List[Union[int, None]] = []
        self.heap_array_size: int = 0
        self.count_elems: int = 0

    def MakeHeap(self, input_array: List[int], depth: int) -> None:
        self.heap_array_size = 2 ** (depth + 1) - 1 if depth >= 0 else 0
        if self.heap_array_size < len(input_array):
            return
        self.HeapArray = [None] * self.heap_array_size
        for key in input_array:
            self.Add(key)

    def GetMax(self):
        if self._is_empty():
            return -1
        root_key = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.count_elems - 1]
        self.HeapArray[self.count_elems - 1] = None
        self.count_elems -= 1
        self._trickle_down(0)
        return root_key
    
    def Add(self, key) -> bool:
        if self._is_full():
            return False
        # Add key to first free slot
        self.HeapArray[self.count_elems] = key
        # 
        self._trickle_up(self.count_elems)
        self.count_elems += 1
        return True
    
    def _is_empty(self) -> bool:
        return self.count_elems == 0
    
    def _is_full(self) -> bool:
        return self.count_elems == self.heap_array_size
    
    def _trickle_down(self, index: int):
        top_key = self.HeapArray[index]
        # Идем вниз, пока у узла есть хотя бы один потомок
        index_new_slot = index
        while index_new_slot < self.count_elems // 2:
            left_child_index = 2 * index_new_slot + 1
            right_child_index = left_child_index + 1
            # Определяем большего потомка
            if (
                right_child_index < self.count_elems - 1 and
                self.HeapArray[left_child_index] < self.HeapArray[right_child_index]
            ):
                larger_child_index = right_child_index
            else:
                larger_child_index = left_child_index
            if top_key >= self.HeapArray[larger_child_index]:
                break
            # Двигаемся на один узел вниз
            self.HeapArray[index_new_slot] = self.HeapArray[larger_child_index]
            index_new_slot = larger_child_index
        self.HeapArray[index_new_slot] = top_key

    def _trickle_up(self, index: int) -> None:
        if index == 0:
            return
        parent_index = (index - 1) // 2
        # Только что вставленный элемент
        inserted_key = self.HeapArray[index]

        # Ищем место в куче для нового узла
        index_new_slot = index
        while index_new_slot > 0 and self.HeapArray[parent_index] < inserted_key:
            # Ставим на место index_new_slot родителя
            self.HeapArray[index_new_slot] = self.HeapArray[parent_index]
            index_new_slot = parent_index
            parent_index = (parent_index - 1) // 2
        self.HeapArray[index_new_slot] = inserted_key
