class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        n = len(nums)
        i = 0
        while i < n and not nums[i] > 0:
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1

        return res