#IF-ELIF-ELSE STATEMENTS - 

light = "green"

if(light == "red"):
    print("STOP")

elif(light == "green"):
    print("GO")

else:
    print("WAIT")

print("End of teaching you basic traffic rules you weird stuffed animal")

#NESTED IF STATEMENTS -

num = int(input("Enter a number : "))

if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")