# conditions
age = 15
if age == 18:
    print("allowed")
else:
    print("not allowed")


#Max of 3 number

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))

if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")
