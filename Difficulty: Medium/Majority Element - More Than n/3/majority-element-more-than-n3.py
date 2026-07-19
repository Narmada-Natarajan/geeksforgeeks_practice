class Solution:
    def findMajority(self, arr):
        # code here
        map={}
        n=len(arr)
        ans=[]
        for i in arr:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
                
        for i in map:
            if map[i]>n//3:
                ans.append(i)
        if ans:
            ans.sort()
            return ans   
        return []
                
            
            
        
            