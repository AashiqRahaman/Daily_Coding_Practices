class Solution {
    public int[] numberGame(int[] nums) {
        Arrays.sort(nums);
        int t=0;
        for (int i = 0; i< nums.length;i+=2){
            t=nums[i];
            nums[i]=nums[i+1];
            nums[i+1]=t;
        }
        return nums;
        
    }
}