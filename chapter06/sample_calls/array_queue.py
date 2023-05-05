

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

#------------------------------------------------------------------------------------------------------------


# Option 2: 

# Code Fragment 6.6: Definition for an Empty exception class.
class Empty(Exception):
    pass


class ArrayQueue:
    CAPACITY = 10
    def __init__(self):
        self._data = [None] * self.CAPACITY                  # 数组数据容量(总存储能力)
        self._size = 0                                       # 当前数组大小                                  
        self._front = 0                                      # self._front为当前数据的第一个索引
    def __len__(self):
        return self._size                                    # 返回当前数据长度
    def is_empty(self):
        return self._size == 0
    def show_first(self):                                    # 定义当前第一个索引的元素
        if self.is_empty():                                  # 若为空，则提出Queue is empty
            raise Empty("Queue is empty")
        else:     
            return self._data[self._front]                   # 若不为空，返回当前队列第一个索引的元素
    def dequeue(self):                                       # dequeue()为出队函数
        if self.is_empty():                  
            raise Empty("Queue is empty")
        showdata = self._data[self._front]                   # 在删除对象的引用之前，显示当前第1个索引值的元素
        self._data[self._front] = None                       # 把None赋值为上述第一索引值的元素，回收未使用空间
        self._front = (self._front + 1) % len(self._data)    # 模运算更新索引，把此前第2个元素变成第1个元素
        self._size -= 1                                      # self._size自减一
        if 0 < self._size < len(self._data) // 4:            # 在当前数据大小下降为数据容量的1/4时
            self._resize(len(self._data) // 2)               # 数据容量减半
        # print(showdata)
        return showdata                                      # 返回showdata
    def enqueue(self, element):                              # enqueue()为入队函数
        if self._size == len(self._data):                    # 若当前数据大小等于数据容量的长度
            self._resize(2 * len(self._data))                # 数据容量倍增
        avail = (self._front + self._size) % len(self._data) # 下一个要插入的位置(即索引)
        # print(avail)                                       # 打印9个数，
        self._data[avail] = element                          # 把element赋值给下一个要插入的位置
        self._size += 1                                      # 当前数据大小自增1
    def _resize(self, cap):                                  # cap >= len(self)
        current = self._data                                 # 跟踪当前列表
        # print(current)
        self._data = [None] * cap                            # 对应上述构造函数中的[None]*CAPACITY
        walk = self._front                                   # 把前队列中的第1个索引赋值为walk索引
        # print(walk)
        for i in range(self._size):                          # 遍历当前数组
            self._data[i] = current[walk]                    # 把当前数组下标求出的值赋给self._data[i]
            walk = (1 + walk) % len(current)                 # 模运算: 求出新的walk索引
            # print(walk)
        self._front = 0                                      # 把0赋值给self._front


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