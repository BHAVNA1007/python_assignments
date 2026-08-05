'''
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''


#using sorting      o(n log n)

nums = [3,2,1,5,6,4]
k = 2

nums.sort(reverse=True)
print(nums[k-1])







#without sorting          o(n*k)
nums = [3,2,1,5,6,4]
k = 2

def kthLargest(nums, k):

   for i in range(k):

       kthlargest = float("-inf")
       index = -1

       for j in range(len(nums)):
    
           if nums[j] > kthlargest:
              kthlargest = nums[j] 
              index = j
       nums[index] = float("-inf")  

   return kthlargest

print("K TH Largest ",kthLargest(nums, k))







'''
Method 2: Min Heap (Recommended)  O(n log k)
Idea

Maintain a heap of only k elements.

The smallest among those k elements is the kth largest overall.
'''

import heapq

nums = [3,2,1,5,6,4]
k = 2

def kthLargest(k, nums):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        
        if len(heap) > k:
           heapq.heappop(heap)

     
    return heap[0]

print(kthLargest(k, nums)) 



      
