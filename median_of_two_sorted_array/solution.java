class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int totalLen = len1+len2;
        int[] merged = new int[totalLen];
        int ptr1=0, ptr2=0;

        for(int i = 0; i< totalLen; i++){
            if(ptr1 >= len1) {
                merged[i] = nums2[ptr2];
                ptr2++;
            }
            else if (ptr2 >= len2){
                merged[i] = nums1[ptr1];
                ptr1++;
            }
            else if(nums1[ptr1] <= nums2[ptr2]) {
                merged[i] = nums1[ptr1];
                ptr1++;
            }
            else{
                merged[i] = nums2[ptr2];
                ptr2++;
            }
        }

        if(totalLen%2 == 0){
            return (merged[totalLen/2] + merged[(totalLen/2)-1])/2.0;
        }
        else{
            return merged[totalLen/2];
        }

    }
}
