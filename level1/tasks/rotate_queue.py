from queue import Queue


def cyclic_shift_queue(queue: Queue):
    end_elem = queue.dequeue()
    queue.enqueue(end_elem)


def rotate_queue(queue: Queue, number_shifts: int):
    for _ in range(number_shifts):
        cyclic_shift_queue(queue)