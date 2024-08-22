#Program statement: Program to Find odd placed digits in a number

input_number = input("Enter the number to find odd place digits:")
odd_placed = []
for i in range(len(input_number)):
    if i%2 == 0:
        odd_placed.append(input_number[i])
print("The odd placed digits are:",odd_placed)