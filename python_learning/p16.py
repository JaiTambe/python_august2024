# Program to reverse a number

input_number = input('Enter a number to reverse : ')
reversed_number=""
input_reduce=int(input_number)

for i in range(len(input_number)):
    digit=input_reduce%10
    reversed_number=reversed_number+str(digit)
    input_reduce=input_reduce//10

print("the reverse number is : ",reversed_number)
