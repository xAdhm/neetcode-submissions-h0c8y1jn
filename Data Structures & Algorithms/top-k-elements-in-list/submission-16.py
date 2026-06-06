class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        groups = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for n, c in freq.items():
            groups[c].append(n)

        for c in range(len(groups) - 1, 0, -1):
            for n in groups[c]:
                res.append(n)

                if len(res) == k:
                    return res