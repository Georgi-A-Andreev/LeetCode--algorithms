
class Solution(object):  # Brute force way
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([2, 4, 6], 6))


class Solution(object):  # More efficient way
    def twoSum(self, nums, target):
        pass