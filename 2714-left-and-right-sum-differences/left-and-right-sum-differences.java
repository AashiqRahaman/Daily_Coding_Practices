class Solution {
    public int[] leftRightDifference(int[] nums) {
        int l = nums.length;
        int[] a = new int[l];
        int[] b = new int[l];


        for (int i = 1; i < l; i++) {
            a[i] = nums[i - 1] + a[i - 1];
        }


        for (int i = l - 2; i >= 0; i--) {
            b[i] = nums[i + 1] + b[i + 1];
        }

        for (int i = 0; i < l; i++) {
            a[i] = Math.abs(a[i] - b[i]);
        }

        return a;
    }
}
