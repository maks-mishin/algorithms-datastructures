from queue import Queue


def cyclic_shift_queue(queue: Queue):
    queue.enqueue(queue.dequeue())


def rotate_queue(queue: Queue, number_shifts: int):
    if queue.size() == 0:
        return
    for _ in range(number_shifts):
        cyclic_shift_queue(queue)
