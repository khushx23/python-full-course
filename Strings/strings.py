#STRING -

str = "This is Khushi Walia." #storing the string
print(str)  #printing the stored value of string

#CONCATENATION : concatenaion is adding two diff strings

str1 = "Khushi"
str2 = "Walia"
sum = str1+str2
print(sum) #output - KhushiWalia

#LENGTH OF STRING
 
print(len(str))  #print the length of any string
print(len(str1))
print(len(str2))  

#Indexing : Indexing in Python accesses elements using position numbers. Positioning starts from 0.
str3 = "PYTHON YAHOO HEHE"
ch = str3[3]
print(ch) #prints H. 0-P , 1-Y , 2-T, 3-H , 4-O...
print(str3[3]) #another method of printing the index of the string

#Slicing : accessing a part of string - str(string name)[0:5] , the last index is excluded , it is not returned in the output

str4 ="WEB DEVELOPMENT"
Slice = str4[0:5] 
print(Slice)
print(str4[0:5]) #we can simply print it in this manner
print(str4[:5]) #leaving the starting index empty would mean that the index is 0.So it is not a wrong input
print(str4[0: ]) #leaving the ending index empty would mean that the index is a no. greater than the last one.So it is not a wrong input
print(str4[0:len(str4)]) #writing the length of str 4 is same as giving the last index , not invalid input



