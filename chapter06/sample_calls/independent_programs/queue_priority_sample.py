

# queue_priority_sample.py

"""
A priority queue data structure is unique from all the other types of the queue because, 
each element has its own priority according to which all the elements are served. Suppose 
if the two elements have the same priority then, they will be served on the basis of their 
order.
"""


class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    # Check whether the demo queue is empty or not
    def is_empty(self):
        return len(self.queue) == 0
    # Add the elements in the demo queue
    def add_element(self, element):
        self.queue.append(element)
    # Remove the elements from the demo queue on the basis of their priority
    def remove_element(self):
        try:
           max = 0
           for i in range(len(self.queue)):
                if self.queue[i] >= self.queue[max]:
                    max = i
                items = self.queue[max]
                del self.queue[max]
                return items
        except IndexError:
            print()
        exit()


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.add_element(11)
    pq.add_element(2)
    pq.add_element(45)
    pq.add_element(72)
    print(pq)         
    while not pq.is_empty():
        print(pq.remove_element())


# Output:

"""
11 2 45 72
11
2
45
72
"""