class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]]
        for i in range(1, len(height)):
            prefix.append(max(prefix[-1], height[i]))

        suffix = [height[-1]]
        for i in range(len(height) - 2, -1, -1):
            suffix.append(max(suffix[-1], height[i]))
        suffix.reverse()

        res = 0
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i]

        return res