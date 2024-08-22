# Program to find biggest(smallest) digit in a number

Input_number = input("Enter a number to find the biggest and smallest digit: ")

biggest = -1
smallest = 9

for last_number in Input_number:
    last_number = int(last_number)
    if last_number > biggest:
        biggest = last_number
    if last_number < smallest:
        smallest = last_number

print(biggest, "is the biggest digit")
print(smallest, "is the smallest digit")
