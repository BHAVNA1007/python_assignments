'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
'''



#basic approch dic + count
'''
nums = [1,2,1,2,1,2,3,1,3,2] 
k = 2

frequency = {}

#freq count

for i in nums:
   count = 0
   for j in nums:
       if i==j:
          count += 1
   frequency[i] = count

print(frequency)

res = []
for kth in range(k):

    most_fre = 0
    most_fre_element = None

    for num in frequency:
        if frequency[num] > most_fre:
            most_fre = frequency[num]
            most_fre_element = num

    res.append(most_fre_element)

    # Remove it so we don't select it again

    del frequency[most_fre_element]

print(res)
'''






#using hashmap4 + sorting  
'''
nums = [1,2,1,2,1,2,3,1,3,2] 
k = 2

frequency = {}

for num in nums:
    frequency[num] = frequency.get(num, 0)+1

#print(frequency ) 

sorted_fre = sorted(frequency,key=frequency.get,reverse=True) 

ans = sorted_fre[:k]
print(ans)
'''







#O(n)  bucket+hashmap


nums = [1,2,1,2,1,2,3,1,3,2] 
k = 2

def topkthElements(nums, k):

   frequency = {}

   for i in nums:
       frequency[i] = frequency.get(i, 0)+1



   #empty list using list comprehenshion named bucket

   buckets = [[] for i in range(len(nums))]

   for num, count in frequency.items():
       buckets[count].append(num)


   ans = []

   for freq in range(len(buckets)-1,0,-1):

      for num in buckets[freq]:

          ans.append(num)

          if len(ans) == k:

             return ans

print(topkthElements(nums, k))

    













                
    
    


