class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1+len2
        ptr1 = 0
        ptr2 = 0
        merged = []

        for i in range(total_len):
            if ptr1 >= len1:
                merged.append(nums2[ptr2])
                ptr2 += 1
            elif ptr2 >= len2:
                merged.append(nums1[ptr1])
                ptr1 += 1
            elif nums1[ptr1] <= nums2[ptr2]:
                merged.append(nums1[ptr1])
                ptr1 += 1
            else:
                merged.append(nums2[ptr2])
                ptr2 += 1

        print(merged)
        if total_len%2:
            return merged[total_len//2]
        else:
            return (merged[total_len//2] + merged[total_len//2 -1])/2

            
