class Solution {
    public int trap(int[] height) {
        int i=0;
        int water=0;
        int j=height.length-1;
        int leftpiller=0;
        int rightpiller=0;
        while(i<j)
        {
            if(height[i]<height[j])
            {
                if(height[i]>leftpiller)
                {
                    leftpiller=height[i];
                }   
                else
                {
                        water+=leftpiller-height[i];
                }
                i++;
                
            }
            else
            {
                if(height[j]>rightpiller)
                {
                    rightpiller=height[j];

                }
                else
                {
                water +=rightpiller-height[j];
                }
                j--;
            }
        }
        return water; 
    }
}