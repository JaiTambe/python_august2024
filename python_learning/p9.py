#Problem statement: Program to print math table of a number

math_number = int(input("Enter any number:"))

math_table_size = int(input("Enter the length of the table:"))

print("Math Table:")

for i in range(1,math_table_size+1):
    number_product = math_number*i
    print('%02d * %02d = %03d'%(math_number,i,number_product))
    number_product = 0
