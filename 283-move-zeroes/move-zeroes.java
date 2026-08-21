class Solution {
    public void swap(int[] nums,int a, int b){
        int temp= nums[a];
        nums[a]=nums[b];
        nums[b]=temp;
    }
    public void moveZeroes(int[] nums) {
        int left = 0;
        for (int i=0;i<nums.length;i++){
            if (nums[i]!=0){
                swap(nums,left,i);
                left++;
            }
        }
        
    }
}