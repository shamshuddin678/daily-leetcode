class Solution {
    public int smallestIndex(int[] nums) {
        for(int i = 0; i< nums.length; i++){
            int digit = nums[i];

            int total = 0;
            while(digit > 0){
                total += digit % 10;
                digit = digit / 10;
            }
            if(total == i){
                return i;
            }
        }
        return -1;
    }
}