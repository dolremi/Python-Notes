import heapq, time
class Solution(object):
    """The problem itself from https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
       Here lists several different solutions from the worst to the best
       :type nums1: List[int]
       :type nums2: List[int]
       :type k: int
       :rtype: List[List[int]]
       """

    @staticmethod
    def raw_solution(nums1, nums2, k):
        rtype = []
        sample = []
        if len(nums1) == 0 or len(nums2) == 0:
            return rtype
        k = min(k, len(nums1) * len(nums2))
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(sample, (nums1[i] + nums2[j], nums1[i], nums2[j]))

        for _ in range(k):
            sum, left, right = heapq.heappop(sample)
            rtype.append([left, right])
        return rtype

    @staticmethod
    def keep_heap(nums1, nums2, k):
        """A solution to keep max-heap with size k"""
        rtype = []
        sample = []
        x = 0
        if len(nums1) == 0 or len(nums2) == 0:
            return rtype
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if x < k:
                    heapq.heappush(sample, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))
                    x += 1
                else:
                    if nums1[i] + nums2[j] < -sample[0][0]:
                        heapq.heappushpop(sample, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))

        rtype = map(lambda x: [x[1], x[2]], sorted(sample, reverse=True))
        return rtype


if __name__ == "__main__":
    left = [1, 4, 5, 6, 7, 19]
    right = [-2, 3, 10, 32, 34]
    result1 = []
    result2 = []
    start_time = time.time()
    result1 = Solution().raw_solution(left, right, 5)
    end_time = time.time()
    print("Raw solution running time was %g seconds" %(end_time - start_time))
    print(result1)
    start_time = time.time()
    result2 = Solution().keep_heap(left, right, 5)
    end_time = time.time()
    print("K size heap solution running time was %g seconds" %(end_time - start_time))
    print(result2)