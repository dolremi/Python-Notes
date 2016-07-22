from __future__ import division

class DaryHeap(object):
    """DaryHeap class represents a D-ary Max-Heap which has d children """
    def __init__(self, items, size):
        self.items = items
        self.heap_size = size

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __len__(self):
        return len(self.items)


def child(i, d, k):
    """The ith child of the current index i"""
    return d * i + k + 1


def parent(i, d):
    return (i - 1) // d


def max_heapify(A, i, d):
    """For d-array heap, one needs to loop through all child"""
    while 1:
        largest = i
        for x in range(d):
            kid = child(i, d, x)
            if kid < A.heap_size and A[kid] > A[largest]:
                largest = kid
        if largest == i:
            return

        A[i], A[largest] = A[largest], A[i]
        i = largest


def extract_max(A, d):
    max_element = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size -= 1
    max_heapify(A, 0, d)
    return max_element


def heap_increase_key(A, i, key, d):
    if key < A[i]:
        raise Exception("new key is smaller than current key")
    A[i] = key

    while i > 0 and A[parent(i, d)] < key:
        A[i] = A[parent(i, d)]
        i = parent(i, d)

    A[i] = key


def heap_increase(A, key, d):
    A.heap_size += 1
    A[A.heap_size - 1] = float("-inf")
    heap_increase_key(A, A.heap_size- 1, key, d)


if __name__ == "__main__":
    items = [12, 23, 43, -23, 43, -23]
