class Solution {
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        int maximumSubarraySum = Integer.MIN_VALUE;
        int start = 0;
        int end = 0;
        
        for (int left =0; left < len; left ++){
            int runningWindowSum = 0;
            
            for (int right = left; right < len; right ++){
                runningWindowSum += nums[right];
                
                if (runningWindowSum > maximumSubarraySum){
                    maximumSubarraySum = runningWindowSum;
                    start = left;
                    end = right;
                }
            }
        }
        return maximumSubarraySum;
    }
}
        