

# array_queue.py


# Option 1: 


# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


# Code Fragment 6.2: Implementing a stack using a Python list as storage.
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10                      # moderate capacity for all new queues
    def __init__(self):
        # Create an empty queue.
        self._data = [None] * self.DEFAULT_CAPACITY # _data: list instance
        self._size = 0  # number of the elements stored in the queue
        self._front = 0 # index of the first element of self._data instance queue
    def __len__(self):
        # Return the number of elements in the queue.
        return self._size
    def is_empty(self):
        # Return True if the queue is empty.
        return self._size == 0
    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    def enqueue(self, e):
        # Add an element to the back of queue.
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1        
    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]       # self_data: list instance
        self._data[self._front] = None         # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    def _resize(self, cap):                    # we assume cap >= len(self)
        # Resize to a new list of capacity >= len(self).
        old = self._data                       # keep track of existing list
        self._data = [None] * cap              # allocate list with new capacity
        walk = self._front
        for k in range(self._size):            # only consider existing elements
            self._data[k] = old[walk]          # intentionally shift indices
            # What is the meanding 1 + walk, walk is self._front? 
            # It take the seond element as the first element 
            walk = (1 + walk) % len(old)       # use old size as modulus
        self._front = 0                        # front has been realigned


if __name__ == '__main__':
    aq = ArrayQueue()
    aq.enqueue(5)
    aq.enqueue(3)
    aq.dequeue()
    aq.enqueue(2)
    aq.enqueue(8)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(9)
    aq.enqueue(1)
    aq.dequeue()
    aq.enqueue(7)
    aq.enqueue(6)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(4)
    aq.dequeue()
    aq.dequeue()


# Output:


"""
5
3
2
8
9
1
7
6

"""
#------------------------------------------------------------------------------------------------------------


# Option 2: 

# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


class ArrayQueue:
    CAPACITY = 10
    def __init__(self):
        self._data = [None] * self.CAPACITY                  # Array capacity for all data
        self._size = 0                                       # Current array size                                 
        self._front = 0                                      # self._front is the 1st index of current data
    def __len__(self):
        return self._size                                    # return the length of current data
    def is_empty(self):
        return self._size == 0
    def show_first(self):                                    # Define the element of  1st index
        if self.is_empty():                                  # Raise Queue is empty if empty
            raise Empty("Queue is empty")
        else:     
            return self._data[self._front]                   # Return the element as 1st index if not empty
    def dequeue(self):                                       
        if self.is_empty():                  
            raise Empty("Queue is empty")
        showdata = self._data[self._front]                   # Show the element as 1st index before deleting object reference
        self._data[self._front] = None                       # Collect non-use space after assign None to the element of array 
        self._front = (self._front + 1) % len(self._data)    # Change the 2nd element to 1st element with updating index with modulo operator
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:            # if current data size decrease 1/4 of the current size
            self._resize(len(self._data) // 2)               # decrease 1/2 data size
        # print(showdata)
        return showdata
    def enqueue(self, element):
        if self._size == len(self._data):                    # if current size is equal to the length of data 
            self._resize(2 * len(self._data))                # double data size
        avail = (self._front + self._size) % len(self._data) # The next position(index) which a next element will be inserted
        # print(avail)                                       
        self._data[avail] = element                          # Assign element to the next index to be inserted
        self._size += 1
    def _resize(self, cap):                                  # cap >= len(self)
        current = self._data                                 # Track the current list
        # print(current)
        self._data = [None] * cap
        walk = self._front                                   # Assign the 1st inex of queue to the index of walk
        # print(walk)
        for i in range(self._size):                          # Traverse the current array
            self._data[i] = current[walk]                    # Assign the gotten value to self._data[i]
            walk = (1 + walk) % len(current)                 # modulo operation: get the new index of walk
            # print(walk)
        self._front = 0


if __name__ == '__main__':
    aq = ArrayQueue()
    aq.enqueue(5)
    aq.enqueue(3)
    aq.dequeue()
    aq.enqueue(2)
    aq.enqueue(8)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(9)
    aq.enqueue(1)
    aq.dequeue()
    aq.enqueue(7)
    aq.enqueue(6)
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(4)
    aq.dequeue()
    aq.dequeue()


# Output:

"""
>>> # print(showdata) - dequeue() method
5
3
2
8
9
1
7
6
>>> # print(avail) - enqueue() emthod 
0
1
>>>
1
2
>>>
3
4
>>>
0
1
>>>
2
>>> # print(current) - _resize() method
[None, 3, None, None, None, None, None, None, None, None]
>>> print(walk) - _resize() method: 1st time
1
>>> print(walk) - _resize() method: 2nd time 
2
>>> # Final value from main() function
5
3
2
8
9
1
7
6
"""

#############################################################################################################


# Option 3: 


class Queue:
    # To initialize the object.
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
    # Function to insert an element
    # at the rear of the queue
    def queueEnqueue(self, data):
        # Check queue is full or not
        if(self.capacity == self.rear):
            print("\nQueue is full")
        # Insert element at the rear
        else:
            self.queue.append(data)
            self.rear += 1
    # Function to delete an element
    # from the front of the queue
    def queueDequeue(self):
        # If queue is empty
        if(self.front == self.rear):
            print("Queue is empty")
        # Pop the front element from list
        else:
            x = self.queue.pop(0)
            self.rear -= 1
    # Function to print queue elements
    def queueDisplay(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
        # Traverse front to rear to
        # print elements
        for i in self.queue:
            print(i, "<--", end='')
    # Print front of queue
    def queueFront(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
        print("\nFront Element is:",
            self.queue[self.front])


# Driver code
if __name__ == '__main__':
    # Create a new queue of
    # capacity 4
    q = Queue(4)
    # Print queue elements
    q.queueDisplay()
    # Inserting elements in the queue
    q.queueEnqueue(20)
    q.queueEnqueue(30)
    q.queueEnqueue(40)
    q.queueEnqueue(50)
    # Print queue elements
    q.queueDisplay()
    # Insert element in queue
    q.queueEnqueue(60)
    # Print queue elements
    q.queueDisplay()
    q.queueDequeue()
    q.queueDequeue()
    print("\n\nafter two node deletion\n")
    # Print queue elements
    q.queueDisplay()
    # Print front of queue
    q.queueFront()


# Output:

"""
Queue is Empty
20 <--30 <--40 <--50 <--
Queue is full
20 <--30 <--40 <--50 <--

after two node deletion

40 <--50 <--
Front Element is: 40
"""