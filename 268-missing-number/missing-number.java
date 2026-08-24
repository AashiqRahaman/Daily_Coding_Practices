class Solution {
    public int missingNumber(int[] nums) {
        byte []arr = new byte[nums.length+1];
        for(int i: nums){
            arr[i] = 1;
        }
        for(int i = 0; i < nums.length; i++){
            if(arr[i] == 0) return i;
        }
        return nums.length;
    }
}