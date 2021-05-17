"""Given an array of integers, return *indices* of the two numbers such that they add up to the specific target

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in index:
                return [i, index[other]]
            index[num] = i
