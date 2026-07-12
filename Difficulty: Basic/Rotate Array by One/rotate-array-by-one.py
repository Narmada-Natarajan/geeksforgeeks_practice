class Solution:
    def rotate(self, arr):
        
        n=len(arr)
        a=arr[-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=a
        return arr
            
    
        #return arr[:]=arr[-1:]+arr[:-1]