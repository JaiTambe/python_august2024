# Program to accept 3 distinct number and find smallest among them

print("Enter the three distinct number")
number_1=int(input('Enter first number :'))
number_2=int(input('Enter second number :'))
number_3=int(input('Enter third number :'))

if number_1<number_2 and number_1<number_3:
    print(f'{number_1} is smallest')
elif number_2<number_3:
     print(f'{number_2} is smallest')
else:
      print(f'{number_3} is smallest')