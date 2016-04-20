__author__ = 'c_disenc'

import random

def bubble_sort(items):
    """ Implementation of quick sort """
    for i in range(0,len(items)):
        for j in range(i+1,len(items)):
            if items[i] > items[j]:
                (items[i],items[j]) = (items[j], items[i])

if __name__ == '__main__':
    random_items = [random.randint(-50, 100) for c in range(10)]

    print ('Before: ', random_items)
    bubble_sort(random_items)        # Replace the funtion name here to
                                        # try any of the other algorithms
    print ('After : ', random_items)
