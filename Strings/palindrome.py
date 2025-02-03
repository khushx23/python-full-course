#palindrome check

str = input("Enter a string : ")
print("The entered string is: ", str)

reverse_str = str[: : -1]

print("Reversed string : ", str[ : :-1])

print("The string is Palindrome if the reversed string is same as the entered string.")

if( str == reverse_str):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")
