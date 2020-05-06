"""
Question - Find the largest number in a list of integers without using built in function max
Answer - 
1) reduce function
2) iteration through the list
3) sorting the list
"""

# Method 1 - reduce function
import functools

mylist = [10,20,3,7,100]
print(functools.reduce(lambda num1,num2: num1 if num1>num2 else num2,mylist))

# Method 2 - iteration through list
maxnum = mylist[0]
for num in mylist:
	if num > maxnum:
		maxnum = num

print(maxnum)


#Method 3 - sorting the list
mylist.sort()
print(mylist[-1])
