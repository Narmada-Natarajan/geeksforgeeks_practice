class Solution:
    def missingNum(self, arr):
        
        #XOR Properties
        #a^a=0
        #a^0=a
        
        n=len(arr)+1
        
        xor1=0
        xor2=0
        
        for i in range(1,n+1):
            xor1^=i
        
        for x in arr:
            xor2^=x
            
        return xor1^xor2