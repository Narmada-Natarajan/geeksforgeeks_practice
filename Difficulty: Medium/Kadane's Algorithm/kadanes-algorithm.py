class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        n=len(arr)
        max_sum=arr[0]
        cur_sum=arr[0]
        
        for i in range(1,n):
            cur_sum=max(arr[i],cur_sum+arr[i])
            max_sum=max(max_sum,cur_sum)
        return max_sum
            