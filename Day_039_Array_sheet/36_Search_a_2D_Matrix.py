'''
74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

'''
#matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

m = int(input("ROWS: "))
n = int(input("COLS: "))

matrix = []

for i in range(m):
    r = []
    for j in range(n):
       v = int(input(f"[{i}][{j}]: "))
       r.append(v)
    matrix.append(r)

#display matrix 

for i in matrix:
   for j in i:
      print(j, end=" ")
   print()
'''


'''
1 2
3 4
'''


'''
for row in matrix:
    print(row)

[1, 2]
[3, 4]
'''



'''
target = int(input("\nEnter target to search: "))

#Solution 1: Brute Force
#The simplest solution is to visit every element.
#Time  = O(m × n)
#Space = O(1)


class Solution:

   def searchMatrix(self, matrix, target):

      for i in matrix:
         for value in i:
            if value == target:
                return True

      return False  
 
obj = Solution()
print(obj.searchMatrix(matrix, target))
'''






'''
Solution 2: Binary Search Row by Row
We can use binary search inside each row.

We perform binary search on every row.
There are m rows, and each binary search takes O(log n).

Time = O(m × log n)
Space = O(1)

'''







'''

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 2


def searchMatrix(matrix, target):
    for row in matrix:

        left = 0
        right = len(row) - 1

        while left <= right:
  
           mid = (left + right) // 2
     
           if row[mid] == target:
               return True

           elif row[mid] < target:
               left = mid + 1

           else:
               right = mid - 1

    return False

print(searchMatrix(matrix, target))

'''








'''
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

def searchMatrix(matrix, target):

      rows = len(matrix)
      cols = len(matrix[0])

      left = 0
      right = rows * cols - 1    

      while left <= right:
 
          mid = (left + right) // 2
          
           
          row = mid // cols
          col = mid % cols

          value = matrix[row][col] 
              
          if  value == target :
              return True

          elif value < target:
               left = mid + 1
 
          else:
               right = mid - 1
  
      return False 

print(searchMatrix(matrix, target))
'''
 



 
'''
There are m × n elements.

Binary search takes:

O(log(m × n))

We don't create another array.

Therefore:

Time Complexity:  O(log(m × n))
Space Complexity: O(1)
'''                 

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 10

#flateennnn + binary

def sm(matrix, target):

    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1
   
    while left <= right:
       mid = (left + right)//2
       
       row = mid // cols
       col = mid % cols

       value = matrix[row][col]
   
       if value == target:
           return True

       elif value < target:
           left = mid + 1
 
       else:
           right = mid - 1 

    return False

print(sm(matrix, target))    















