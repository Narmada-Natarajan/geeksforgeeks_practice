class Solution:
    def getPairs(self, arr):
        # code here
        map={}
        ans=[]
        
        for i in arr:
            if(i in map):
                map[i]=map[i]+1
            else:
                map[i]=1
        
        for x in map:
            if x>0 and -x in map:
                ans.append([-x,x])
        
            if x==0 and map[0]>=2:
                ans.append([0,0])
        ans.sort()
        return ans      
            
                
        
            
        