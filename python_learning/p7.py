# Problem statement: Program to check if the number is Perfect square

number = int(input("Enter a number: "))

sqrt = number ** 0.5

if sqrt.is_integer():
    print(f"{number} is a perfect square.")



