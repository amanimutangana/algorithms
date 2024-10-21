import pytest
from data_structures.queue import Queue

def test_queue_operations():
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.size() == 2
    assert queue.front() == 2
