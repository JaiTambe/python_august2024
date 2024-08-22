# Program to Find count of digits of a number

Input_number = input("Enter a number to find the count of digits: ")

split_num = list(Input_number)

count = 0

for i in split_num:
    count += 1

print('Count of digits of the number:', count)
