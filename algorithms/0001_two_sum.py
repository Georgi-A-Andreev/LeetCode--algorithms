
class Solution(object):  # Brute force way
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([2, 4, 6], 6))


class Solution(object):  # More efficient way
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict:
                return [dict[complement], i]
            dict[nums[i]] = i


print(Solution().twoSum([2, 4, 6], 6))
