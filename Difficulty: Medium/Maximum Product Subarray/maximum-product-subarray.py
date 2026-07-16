class Solution:
	def maxProduct(self,arr):
		# code here
		
		curr_min=arr[0]
		curr_max=arr[0]
		prod_max=arr[0]
		
		for i in range(1,len(arr)):
		
		    temp=max(arr[i],curr_min*arr[i],curr_max*arr[i])
		
		    curr_min=min(arr[i],curr_min*arr[i],curr_max*arr[i])
		    
		    curr_max=temp
		
		    prod_max=max(prod_max,curr_max)
		
	    return prod_max
		
		