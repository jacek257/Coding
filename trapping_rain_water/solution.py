class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        size = len(height)
        potential = [0] * size
        water = 0

        for i in range(size):
            max_height = max(height[size-i-1], max_height)
            potential[size-i-1] = max_height

        max_height = 0
        for i in range(size):
            max_height = max(height[i], max_height)

            water += min(potential[i], max_height) - height[i]

        return water
