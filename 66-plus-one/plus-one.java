class Solution {

    public int[] plusOne(int[] digits) {
        int l = digits.length;
        if (digits[l - 1] != 9) {
            digits[l - 1] = digits[l - 1] + 1;
            return digits;
        } else {
            for (int i = l - 1; i >= 0; i--) {
                if (digits[i] == 9) {
                    digits[i] = 0;
                } else {
                    digits[i] = digits[i] + 1;
                    return digits;
                }
            }
        }
        int[] arr = new int[l + 1];
        arr[0] = 1;
        return arr;
    }
}