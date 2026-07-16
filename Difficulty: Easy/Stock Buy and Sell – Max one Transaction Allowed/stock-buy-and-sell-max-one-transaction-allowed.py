class Solution:
    def maxProfit(self, prices):
        # code here
        #buy at min price
        mini=float('inf')
        ans=0
        
        for i in prices:
            if(i<mini):
                mini=i
            ans=max(ans,i-mini)
        return ans
        