class Solution:
    def countZeroes(self, arr):
        # code here
        cnt=0
        for i in range(len(arr)):
            if arr[i]==0:
                cnt+=1
        return cnt
            
        