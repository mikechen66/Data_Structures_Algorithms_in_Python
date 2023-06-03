

# queue_circular_sample.py


"""
In the circular queue data structure, the last element of the queue is assigned as the 
first element of a queue to make a circular link between the items i.e. we can add the 
new element at the first position.
"""


class CircularQueue():
    def __init__(self, a):
        self.a = a
        self.queue = [None] * a
        self.head = self.tail = -1
    # Add an element into the demo circular queue
    def enqueue(self, element):
        if ((self.tail + 1) % self.a == self.head):
            print("The demo circular queue does not have more space\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = element
        else:
            self.tail = (self.tail + 1) % self.a
            self.queue[self.tail] = element
    # Remove an element from the demo circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The demo circular queue is empty\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.a
            return temp
    def show_result(self):
        if(self.head == -1):
            print("No element present in the demo circular queue")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.a):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
        print()


if __name__ == '__main__':
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    print("Demo Queue")
    cq.show_result()
    cq.dequeue()
    print("Demo Queue after removing the elements")
    cq.show_result()


# Output:

"""
Demo Queue
12345

1
Demo Queue after removing the elements
2345
"""