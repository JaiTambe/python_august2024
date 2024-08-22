# Program to find sum of digits of a number

Input_number = input("Enter a number to find the sum of its digits: ")

split_num = list(Input_number)

sum = 0

for i in split_num:
    sum += int(i)

print(sum)
