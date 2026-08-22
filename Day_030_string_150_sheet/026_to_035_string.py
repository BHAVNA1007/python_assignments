'''
026_to_035_string

26. Find the first occurrence of a word in a string.
27. Find the last occurrence of a word in a string.
28. Count occurrences of a word in a string.
29. Remove the first, last, or all occurrences of a word.
30. Replace a word with another word.
31. Remove duplicate words from a string.
32. Count the frequency of each word in a string.
33. Find the longest word in a string.
34. Find the shortest word in a string.
35. Find the first word that is a palindrome.
'''
#26. Find the first occurrence of a word in a string.
#S = "Test this test", Word = "test" 10 (index)
'''
s = input('Enter the string: ')
word = input('Enter a word: ')

index = -1
for i in range(len(s)-len(word)+1):
    match = True

    for j in range(len(word)):

       if s[i+j] != word[j]:
           match = False
           break

    if match:
       index = i
       break   
print(index)
'''


#27. Find the last occurrence of a word in a string.
#"Test this test test", Word = "test" 15 (index)
'''
s = input('Enter the string: ')
word = input('Enter a word: ')

index = -1

for i in range(len(s)-len(word)+1):
    match = True
  
    for j in range(len(word)):
       if s[i+j] != word[j]:
           match = False
           break

    if match:
        index = i
       
print(index)
'''
'''
#28. Count occurrences of a word in a string.
#S = "word word other word", Word = "word" 3

s = input('Enter the string: ')
w = input('Enter a word: ')
words = s.split()
count = 0

for i in range(len(words)):
    if words[i] == w:
        count += 1

print(count) 
'''

'''
#29. Remove the first, last, or all occurrences of a word.
#S = "a test b test c", Word = "test", Remove All "a b c"

s = input('Enter the string: ')
w = input('Enter the word: ')

words = s.split()
for i in range(len(words)):
    if words[i] != w:
       print(words[i],end=" ")
'''

'''
#30. Replace a word with another word.
#S = "old data", Old="old", New="new" "new data"

s = input('Enter a string: ')

s1 = s.replace("Old","old")
s2 = s.replace('New','new')
#print(s1)
print(s2)
'''

'''
#31. Remove duplicate words from a string.
#S = "the cat and the dog" "the cat and dog

s = input('Enter the string: ')
s1 = s.split()

visit = ''

for i in range(len(s1)):
   
  if s1[i] not in visit:  
     visit += s1[i] + ' '
 
print(visit, end=" ")
'''

'''
#32. Count the frequency of each word in a string.
#S = "apple banana apple" apple: 2, banana: 1

s = input('Enter the string: ')
s1 = s.split()
visit = ''
for i in range(len(s1)):
    count = 0
    if s1[i] not in visit:

       for j in range(len(s1)):

          if s1[i] == s1[j]:
             count += 1
          
       print(s1[i],count)
       visit += s1[i]+' ' 
'''

'''
#33. Find the longest word in a string.
#S = "find the longest word" "longest"

s = input('Enter the string: ')
s1 = s.split()

long = ''

for i in range(len(s1)):
   temp = ''
  
   if len(s1[i]) >len(long):
      temp += s1[i] 
      long = temp

print(long)
   
'''

'''
#34. Find the shortest word in a string.
#S = "find the shortest word" "the"

s = input('Enter the string: ')
s1 = s.split()


short = s1[0] 
for i in range(len(s1)):
   
   temp = ''
  
   if len(s1[i]) <len(short):
      temp += s1[i] 
      short= temp

print(short)
'''
#35. Find the first word that is a palindrome.
#S = "this madam is here" "madam"

s = input('Enter the string:  ')
s1 = s.split()

for i in range(len(s1)):
   word = s1[i]
   for j in range(len(s1)):
      rev = word[::-1]    
      
   if rev == word:
      print(s1[i])     
      break
   

               












       