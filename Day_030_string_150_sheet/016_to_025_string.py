'''
016_to_025_string

16. Count total occurrences of a character in a string.
17. Remove the first, last, or all occurrences of a given character.
18. Replace the first, last, or all occurrences of a character.
19. Find the highest frequency character in a string.
20. Find the lowest frequency character in a string.
21. Find the first non-repeating character.
22. Find the last repeating character.
23. Print all characters that occur exactly twice.
24. Check if all characters in a string are unique (no repetition).
25. Count total number of words in a string.
'''
'''
#16. Count total occurrences of a character in a string.
s = input('Enter the string: ')
ch = input('Enter the char: ')
count = 0
for i in range(len(s)):
    if s[i] == ch:
       count += 1
print('Occurence: ',count) 
'''

'''
#17. Remove the first, last, or all occurrences of a given character.
s = input('Enter the string: ')
ch = input('Enter the char: ')
s1 =''
for i in range(len(s)):
    if s[i] != ch:
       s1 += s[i]
print(s1) 
'''

'''
#18. Replace the first, last, or all occurrences of a character.

s = input('Enter The string: ')
print(s.replace("p","x"))   
'''

'''
#19. Find the highest frequency character in a string.
s = input('Enter The string: ')
h_freq = ''
for i in range(len(s)):
   count = 0
   temp ='' 
   for j in range(i+1,len(s)):
       if s[j] == s[i]:
          temp += s[i]
          count += 1
      
   if len(temp)>len(h_freq):
       h_freq = temp
       print(s[i])  
'''

'''
#20. Find the lowest frequency character in a string.

s = input('Enter the string: ')
lowest_freq = s

for i in range(len(s)):
    count = 0
    temp = ''
    for j in range(len(s)):
        if s[j] == s[i]:
           temp += s[i]
           count += 1
    if len(temp) < len(lowest_freq):
         lowest_freq = temp

print('lowest frequency word is : ', lowest_freq[0])
'''

'''
#21. Find the first non-repeating character.
'''

'''
s = input('Enter the string: ')

f = 0

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
           count += 1
           
    if count == 1:
       print('Non repeating char is: ',s[i])
       f = 1
       break
if f==0:
    print('not non rep') 
'''

'''
#22. Find the last repeating character.
s = input('Enter the string: ')

last = ''

for i in range(len(s)):
            
    for j in range(len(s)):
            
        if s[i] == s[j]:
            
            last = s[i]
            break
            
print('Last repeating character:', last)

'''
'''
#23. Print all characters that occur exactly twice.

s = input('Enter the string: ')

for i in range(len(s)):
   count = 1
   for j in range(i+1,len(s)):
       if s[i] == s[j]:
          count += 1
   if count == 2:
       print(s[i],end=',')
'''

'''
#24. Check if all characters in a string are unique (no repetition).
s = input('Enter a string: ')

f = True

for i in range(len(s)):
    
    for j in range(i+1,len(s)):
       if s[i] == s[j]:
           f = False

if f == True:
   print('True')  
else:
   print('False')                   
     
'''
#25. Count total number of words in a string.
'''
s = input('Enter the string: ')
words = s.split()

count = 0
for i in range(len(words)):
    count+= 1

print(count)

'''
s = input('Enter the string: ')

last = ''

for i in range(len(s)):
            
    for j in range(len(s)):
            
        if s[i] == s[j]:
            
            last = s[i]
            break
            
print('Last repeating character:', last)

             

          
  
       
 




                

