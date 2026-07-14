class Solution:
    def majorityElement(self, arr):
        #code here
        
        #Moore Voting Algorithm 
        
        n=len(arr)
        ele=arr[0]
        cnt=1
        
        for i in range(1,n):
            if(arr[i]==ele):
                cnt+=1
            else:
                cnt-=1
                
            if cnt==0:
                ele=arr[i]
                cnt=1
                
        cnt = 0
        for x in arr:
            if x == ele:
                cnt += 1

        if cnt > n // 2:
            return ele
        return -1
                
        