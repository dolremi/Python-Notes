from __future__ import division
import heapq


def find_min_time():
    n = int(input())
    x = sorted(list(map(int, raw_input().split())) for _ in range(n))

    time = 0
    total_time = 0
    queue = []

    while x or queue:
        while x and (not queue or x[0][0] < time):
            t, l = x.pop(0)
            heapq.heappush(queue, (l, t))
            time = max(time, t)

        l, t = heapq.heappop(queue)
        time += l
        total_time += time - t

    print (total_time // n)


if __name__ == "__main__":
    find_min_time()