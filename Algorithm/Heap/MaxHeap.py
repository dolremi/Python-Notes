from __future__ import division


class heap(object):
    """A.heap_size represents how many elements in the heap that are stored within the array
       len(A) give the number of elements in the array.
       From definition, 0 <= A.heap_size <= len(A)"""
    def __init__(self, items, size):
        self.items = items
        self.heap_size = size or len(items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __len__(self):
        return len(self.items)


def left(i):
    """Left child of index i"""
    return 2 * i + 1


def right(i):
    """Right child of index i"""
    return 2 * i + 2


def parent(i):
    """Parent of index i"""
    return (i - 1) // 2


def max_heapify(A, i):
    """This function use the iterative version which is more efficient"""
    while 1:
        l = left(i)
        r = right(i)

        if l < A.heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i

        if r < A.heap_size and A[r] > A[i]:
            largest = r
        else:
            largest = i

        if largest == i:
            return

        A[i], A[largest] = A[largest], A[i]
        i = largest


def build_max_heap(A):
    A.heap_size = len(A)
    for i in range(len(A) // 2, -1, -1):  # here  len(A) = A.length - 1
        max_heapify(A, i)


def heap_increase_key(A, i, key):
    """This function use the idea of insertion sort to reduce to one assignment inside the loop"""
    if key < A[i]:
        raise Exception("new key is smaller than current key")
    A[i] = key

    while i > 0 and A[parent(i)] < key:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key


def max_heap_insert(A, key):
    A.heap_size += 1
    A[A.heap_size - 1] = float("-inf")
    heap_increase_key(A, A.heap_size - 1, key)


def build_max_heap2(A):
    A.heap_size = 1
    for i in range(1, len(A)):
        max_heap_insert(A, A[i])