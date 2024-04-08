#Given an array arr of size n, the task is to find the maximum triplet product in the array.
class Solution:
    def maxTripletProduct (self, arr,  n): 
        #Complete the function
        
        arr.sort()
        p1=arr[n-1]*arr[n-2]*arr[n-3]
        p2=arr[0]*arr[1]*arr[n-1]
    
        return max(p1,p2)
