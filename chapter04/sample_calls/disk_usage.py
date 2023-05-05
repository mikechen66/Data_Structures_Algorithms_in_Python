
# disk_usage.py

import os


def disk_usage(path):
    # Return the number of bytes used by a file/folder and any descendents.
    total = os.path.getsize(path)                    # account for direct usage
    if os.path.isdir(path):                          # if this is a directory,
        for filename in os.listdir(path):            # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath)           # add child's usage to total
    print ('{0:<7}'.format(total), path)             # descriptive output (optional)
    return total                                     # return the grand total


if __name__ == '__main__':
    path = '/home/user/Documents/data_structures_and_algorithm/data_structures_algo/ch04_recursion'
    disk_usage(path)