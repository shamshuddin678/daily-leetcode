class Solution {
    public int thirdMax(int[] nums) {
        Long max = null;
        Long sec = null;
        Long third = null;
        for(int i = 0; i < nums.length; i++) {

            if ((max != null && nums[i] == max) ||
                (sec != null && nums[i] == sec) ||
                (third != null && nums[i] == third)) {
                continue;
            }

            if(max == null || nums[i] > max) {
                third = sec;
                sec = max;
                max = (long) nums[i];
            }
            else if(sec == null ||(nums[i] < max && nums[i] >= sec) ) {
            third = sec;
            sec = (long) nums[i];
            }
            else if(third == null || (nums[i] < sec && nums[i] >= third && nums[i] < max )) {
                third = (long) nums[i];
            }
        }
        
        return third == null ? max.intValue():third.intValue();
    }
}