class Solution:
    def maxConsecBits(self, arr):
        #code here 
        
        ones=0
        zeroes=0
        maxi=0
        
        
        for i in arr:
            if i==1:
                ones+=1
                zeroes=0
            else:
                zeroes+=1
                ones=0
            maxi=max(maxi,ones,zeroes)
        
        return maxi
            
                