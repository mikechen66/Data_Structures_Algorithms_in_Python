


# deque_sample.py


from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, item):
        self._items.append(item)
    def dequeue(self):
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None
    def __len__(self):
        return len(self._items)
    def __contains__(self, item):
        return item in self._items
    def __iter__(self):
        yield from self._items
    def __reversed__(self):
        yield from reversed(self._items)
    def __repr__(self):
        return f"Queue({list(self._items)})"


if __name__ == '__main__':
    numbers = Queue()
    print(numbers)
    # Enqueue items
    for number in range(1, 5):
        numbers.enqueue(number)
    print(numbers)
    print(len(numbers))
    # Support membership tests
    2 in numbers
    10 in numbers
    # Normal iteration
    for number in numbers:
        print(f"Number: {number}")


# Output:


"""
Queue([])
Queue([1, 2, 3, 4])
4
True
False
Number: 1
Number: 2
Number: 3
Number: 4
"""
