num = int(input("Enter a number: "))
fact = 1
while num > 1:
    fact = num * fact
    num = num - 1
#    print(fact)

for i in range(1, num + 1):
    fact = fact * i
print(fact)
