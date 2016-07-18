from __future__ import division, absolute_import, print_function
import heapq


class MedianCalculator:
    """This class dynamically track down the median of the streaming of data,
       it consists of two heaps: one min-heap called upper_half and max-heap called lower_half,
       keep the number of lower_half at most one element more than upper_half
       and the elements in lower_half is no larger than that in upper_half
       the max heap can be implemented as heapq with inverted values"""
    def __init__(self):
        self.upper_half = []
        self.lower_half = []
        self.median = 0

    def insert(self, element):
        if len(self.upper_half) == len(self.lower_half):
            heapq.heappush(self.lower_half, -heapq.heappushpop(self.upper_half, -element))
        else:
            heapq.heappush(self.upper_half, -heapq.heappushpop(self.lower_half, element))

    def get_median(self):
        upper_len = len(self.upper_half)
        lower_len = len(self.lower_half)
        if lower_len > upper_len:
            self.median = self.lower_half[0]
        else:
            self.median = (self.lower_half[0] - self.upper_half[0])/2.0
        return self.median


if __name__ == "__main__":
    track = MedianCalculator()
    sample = [15, 9, 25, -34, 45, 56]
    for i in sample:
        track.insert(i)
        print("The median of the list is {0}".format(track.get_median()))

