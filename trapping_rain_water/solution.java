class Solution {
    public int trap(int[] height) {
        int size = height.length;
        int[] potential = new int[size];
        int max_height = 0;
        int water = 0;

        for (int i=0; i < size; i++) {
            max_height = Math.max(max_height, height[i]);
            potential[i] = max_height;
        }

        max_height = 0;
        for (int i = size-1; i >= 0; i--) {
            max_height = Math.max(max_height, height[i]);

            water += Math.min(potential[i], max_height) - height[i];
        }

        return water;
    }
}
