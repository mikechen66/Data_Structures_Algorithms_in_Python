

# priority_queue_heapq.py


import heapq

class My_PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        """
        The queue consists of (priority, index, item) forms
        The "-" sign is added to priority because heappush is the minimum heap by default
        index is used to arrange two objects in insertion order when they have the same priority
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    def qsize(self):
        return len(self._queue)
    def empty(self):
        return True if not self._queue else False


class Car(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __repr__(self):
        return "{0} -- {1}".format(self.name, self.value)


if __name__ == "__main__":
    car1 = Car("BMW", 45)
    car2 = Car("Maybach", 145)
    car3 = Car("Bugatti", 85)
    car4 = Car("Cadillac", 78)
    car5 = Car("Maserati", 85)
    pq = My_PriorityQueue()
    pq.push(car1, car1.value)
    pq.push(car2, car2.value)
    pq.push(car3, car3.value)
    pq.push(car4, car4.value)
    pq.push(car5, car5.value)
    print("Queue size：{0}".format(pq.qsize()))
    while not pq.empty():
        print(pq.pop())


# Output:

"""
Queue size：5
Maybach -- 145
Bugatti -- 85
Maserati -- 85
Cadillac -- 78
BMW -- 45
"""