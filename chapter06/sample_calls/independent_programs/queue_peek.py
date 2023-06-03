

# queue_peek.py

"""
The name of the function is ‘peek’, and it accepts only one argument – self. Inside 
the function body, we shall print the list queue with index as ‘self.front’.
"""


class Queue:
    def __init__(self,size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size
    def enqueue(self, item):
        if self.available == 0:
            print('Queue Overflow!')
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -= 1
    def dequeue(self):
        if self.available == self.size:
            print('Queue Underflow!')
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1
    def peek(self):
        print(self.queue[self.front])
    def show_queue(self):
        print(self.queue)


if __name__ == '__main__':
    queue1 = Queue(4)
    queue1.enqueue(10)
    queue1.peek()
    queue1.enqueue(20)
    queue1.dequeue()
    queue1.peek()
    queue1.show_queue()


# Output:

"""
10
20
[None, 20, None, None]
"""