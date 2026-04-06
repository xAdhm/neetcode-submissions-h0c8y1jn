class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freqGroups = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, cnt in freq.items():
            freqGroups[cnt].append(num)

        res = []

        for group in range(len(freqGroups) - 1, 0, -1):
            for num in freqGroups[group]:
                res.append(num)
                if len(res) == k:
                    return res