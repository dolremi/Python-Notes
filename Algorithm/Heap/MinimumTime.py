from __future__ import division
import heapq


def find_min_time():
    """ This function calculates the minimum waiting time for all the jobs
        Each job order has an arrival time t and the processing time l
        The input format would be like
        3
        0  9
        1  6
        2  5
        The first number would be number of lines
        then the consequence lines has the format of t  l
        Note that the arrival time may not be in order, thus it needs to sort by arrival time at first
        Then the algorithm would push the arrival time and the processing time in a min-heap if the heap is empty
        or the next job arrival time is before the finish time of the previous one
        Then pop up the job order to calculate the total time"""
    n = int(input())
    x = sorted(list(map(int, raw_input().split())) for _ in range(n))

    time = 0
    total_time = 0
    queue = []

    while x or queue:
        while x and (not queue or x[0][0] < time):
            # if queue is empty or next order comes before the previous order finish time
            t, l = x.pop(0)
            heapq.heappush(queue, (l, t))
            time = max(time, t)

        l, t = heapq.heappop(queue)
        time += l
        total_time += time - t

    print (total_time // n)


if __name__ == "__main__":
    find_min_time()