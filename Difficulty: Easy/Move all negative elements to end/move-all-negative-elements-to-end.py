class Solution:
    def segregateElements(self, arr):
        # code here
        p=[]
        n=[]
        
        for i in arr:
            if i>=0:
                p.append(i)
            else:
                n.append(i)
        arr[:]=p+n