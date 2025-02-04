#LIST IN PYTHON - (they are like the "arrays")

MARKS1 = "45"
MARKS2 = "35"
MARKS3= "54"
MARKS4 = "75"
MARKS5 = "52"

print(MARKS1 , MARKS2, MARKS3 , MARKS4 , MARKS5)

#now here we can use our lists nd tuples...

marks =[] #this is how we initialize it , using square brackets [] , and we separate the values entered inside it using the commas

MARKS = [45,35,54,75,52]

print(MARKS)
print(type(MARKS))
print(MARKS[0:2]) #indexing
 
#indexing works similar to the array , we can access the 0th value..

print(MARKS[0]) #45
print(MARKS[1])  #35
print(MARKS[2])  #54
print(MARKS[3])  #75

#Difference b/w strings nd list, string is immutable (cannot be changed) , lists are mutable

str = "HELLO"
print(str[2])
# str[2] = "t"   #Since, the strings are immuatable the value will not be assigned

student = ["karan" , 18 , 155]
print(student[0])

student[0] = "arjun" #Since lists are mutable , the new value will be assigned
print(student[0])

#LIST METHODS - list "methods" are specifically for list , these functions can only be used in a list.

#1- list.append - adds an element to the list

student.append("LUCKNOW")
print(student) #['karan' , 18 , 155 , 'LUCKNOW']

#2- list.sort - sorts in ascending order

MARKS.sort()
print(MARKS)

#3 - list.sort(reverse=true) - sort in descending order

MARKS.sort(reverse=True)
print(MARKS)

#4 - list.reverse - reverses the original list

student.reverse()
print(student) 

#5 - list.insert(idx,el) -use  to insert any value in the middle of the string , idx - (at what index we want to add the value) , el - what value we want to add

MARKS.insert(3,789)
print(MARKS)

#6 - list.remove(el) - removes the first occurrence of the element(el)

MARKS.remove(75)
print(MARKS)

