class Solution:
    def maxWater(self, arr):
        # code here
        
        n=len(arr)
        prefix=[0]*n
        sufix=[0]*n
        
        maxi=-1
        for i in range(n):
            if(arr[i]>maxi):
                maxi=arr[i]
            prefix[i]=maxi
            
        maxi=-1
        for i in range(n-1,-1,-1):
            if (arr[i]>maxi):
                maxi=arr[i]
            sufix[i]=maxi
        
        res=0
        for i in range(n):
            p=prefix[i]
            s=sufix[i]
            val=min(p,s)
            val=(val-arr[i])
            if(val>0):
                res+=val
        return res
        