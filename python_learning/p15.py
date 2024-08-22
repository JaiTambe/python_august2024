#Program statement: Program to Find sum even(odd) digits in a number

Input_number= input("Enter number to find the sum of its even digits:")
sum_digits = 0
for i in Input_number:
    if int(i)%2 == 0:
        sum_digits += int(i)
print("The sum of even digits in",Input_number,"is",sum_digits)
