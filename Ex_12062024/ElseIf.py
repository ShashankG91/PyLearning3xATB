# write a program that calculates and display grade
# given numerical scores (A,B,C,D,F)
# Input score - 89
# A = 90-100
# B = 80-89
# C = 70-79
# D = 60-69
# F = 0-59

score = int(input("Enter the score :"))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("F")
else:
    print("Invalid score")
