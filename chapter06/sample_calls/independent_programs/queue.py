

# queue.py


from queue import Queue
import random
import threading
import time


# producer thread
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue
    def run(self):
        for i in range(5):
            print ("%s: %s is producing %d to the queue!" %(time.ctime(), self.getName(), i))
            self.data.put(i)       # Put the produced data into queue
            time.sleep(random.randrange(10)/5)
        print ("%s: %s finished!" %(time.ctime(), self.getName()))


# consumer thread
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue
    def run(self):
        for i in range(5):
            val = self.data.get()  # Take the produced data
            print ("%s: %s is consuming. %d in the queue is consumed!" %(time.ctime(), self.getName(), val))
            time.sleep(random.randrange(5))
            self.data.task_done()  # Tell the task is completed
        print ("%s: %s finished!" %(time.ctime(), self.getName()))


# main thread
def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    queue.join()                   # Block until all the data produced by the producer is consumed
    producer.join()                # Wait for the ending of consumer thread
    consumer.join()                # Wait for the ending of consumer thread
    print ('All threads are terminated!')


if __name__ == '__main__':
    main()


# Output:

"""
Wed May 17 20:28:54 2023: Pro. is producing 0 to the queue!
Wed May 17 20:28:54 2023: Con. is consuming. 0 in the queue is consumed!
Wed May 17 20:28:54 2023: Pro. is producing 1 to the queue!
Wed May 17 20:28:54 2023: Con. is consuming. 1 in the queue is consumed!
Wed May 17 20:28:56 2023: Pro. is producing 2 to the queue!
Wed May 17 20:28:56 2023: Con. is consuming. 2 in the queue is consumed!
Wed May 17 20:28:57 2023: Pro. is producing 3 to the queue!
Wed May 17 20:28:58 2023: Con. is consuming. 3 in the queue is consumed!
Wed May 17 20:28:58 2023: Pro. is producing 4 to the queue!
Wed May 17 20:29:00 2023: Pro. finished!
Wed May 17 20:29:00 2023: Con. is consuming. 4 in the queue is consumed!
Wed May 17 20:29:04 2023: Con. finished!
All threads are terminated!
"""