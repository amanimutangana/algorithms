import pytest
from data_structures.stack import Stack

def test_stack_operations():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.peek() == 2
