

# queue_simple_demo.py


class DemoQueue:
    def __init__(self):
        self.items = []
    def is_empty(self): # This function will check whether the queue is empty or not
        return self.items == []
    def enqueue(self, data):
        self.items.append(data) # here we are appending the elements in the queue
    def dequeue(self):
        return self.items.pop(0) # here we are performing the Dequeue operation 


if __name__ == '__main__':
    dq = DemoQueue()
    while True:
        print('Enqueue operation ')
        print('Dequeue operation’')
        print('Quit')
        task = input('What would you like to do? ').split()
        operations = task[0].strip().lower()
        if operations == 'Enqueue': # Condition
            dq.enqueue(int(task[1]))  # Append the element in the queue
        elif operations == 'Enqueue':
            if dq.is_empty():
                print('Demo Queue is empty.')
            else:
                print('Dequeued value: ', dq.dequeue())
        elif operations == 'Quit':
            break


# Output:

"""
Enqueue operation 
Dequeue operation’
Quit
What would you like to do? 
"""
