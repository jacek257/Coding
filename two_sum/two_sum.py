"""Given an array of integers, return *indices* of the two numbers such that they add up to the specific target

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

class Solution:
    def twoSum(self, nums, target):
        index = {}
        for i in range(len(nums)):
            num = nums[i]
            other = target - num
            if other in index.keys():
                return [i, other]
            index[num] = i
