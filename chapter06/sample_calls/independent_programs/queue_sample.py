

# queue_simple.py

"""
In the simple queue data structure, the insertion of the element takes place at the rear 
and removes from the front position. It follows the FIFO criteria.
"""


class Queue:
    def __init__(self):
      self.queue = list()
    def add_element(self, element):
        # Add the above method to insert the element
        if element not in self.queue:
            self.queue.insert(0, element)
            return True
        return False
    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.add_element("Monday")
    q.add_element("Tuesday")
    q.add_element("Wednesday")
    print(q.size())


# Output:

"""
True
True
True
3
"""

