
# Define MinMax class 


class MinMax:
    def __init__(self, data):
        self.data = data 
    def find_max(self):
        # Return the maximum element from a nonempty Python list.
        biggest = self.data[0]          # The initial value to beat
        for val in self.data:           # For each value:
            if val > biggest:           # if it is greater than the best so far,
                biggest = val           # we have found a new best (so far)
        return biggest                  # When loop ends, biggest is the max
    def find_min(self):
        # Return the maximum element from a nonempty Python list.
        smallest = self.data[0]         # The initial value to beat
        for val in self.data:           # For each value:
            if val < smallest:          # if it is greater than the best so far,
                biggest = val           # we have found a new best (so far)
        return smallest                 # When loop ends, biggest is the max


if __name__ == '__main__':
    data = [0,1,2,3,4,5,6,7,8,9]
    mm = MinMax(data)
    max_number= mm.find_max()
    print(max_number)
    min_number = mm.find_min()
    print(min_number)


# Output:

"""
9
0
"""

###############################################################################################


# Define MinMax class without the method of __init__()


class MinMax:
    # def __init__(self):
        # self.data = data 
    def find_max(self, data):
        # Return the maximum element from a nonempty Python list.
        biggest = data[0]          # The initial value to beat
        for val in data:           # For each value:
            if val > biggest:      # if it is greater than the best so far,
                biggest = val      # we have found a new best (so far)
        return biggest             # When loop ends, biggest is the max
    def find_min(self, data):
        # Return the maximum element from a nonempty Python list.
        smallest = data[0]         # The initial value to beat
        for val in data:           # For each value:
            if val < smallest:     # if it is greater than the best so far,
                biggest = val      # we have found a new best (so far)
        return smallest            # When loop ends, biggest is the max


if __name__ == '__main__':
    data = [0,1,2,3,4,5,6,7,8,9]
    mm = MinMax()
    max_number= mm.find_max(data)
    print(max_number)
    min_number = mm.find_min(data)
    print(min_number)


# Output:

"""
9
0
"""

###############################################################################################


class MinMax:
    def __init__(self):
        pass
    def find_max(self, data):
        # Return the maximum element from a nonempty Python list.
        biggest = data[0]          # The initial value to beat
        for val in data:           # For each value:
            if val > biggest:      # if it is greater than the best so far,
                biggest = val      # we have found a new best (so far)
        return biggest             # When loop ends, biggest is the max
    def find_min(self, data):
        # Return the maximum element from a nonempty Python list.
        smallest = data[0]         # The initial value to beat
        for val in data:           # For each value:
            if val < smallest:     # if it is greater than the best so far,
                biggest = val      # we have found a new best (so far)
        return smallest            # When loop ends, biggest is the max


if __name__ == '__main__':
    data = [0,1,2,3,4,5,6,7,8,9]
    mm = MinMax()
    max_number= mm.find_max(data)
    print(max_number)
    min_number = mm.find_min(data)
    print(min_number)


# Output:

"""
9
0
"""