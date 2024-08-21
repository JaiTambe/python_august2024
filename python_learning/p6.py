# Program statement: Program to check if the Alphabet is uppercase

alphabet = input("Enter any alphabet: ")

if len(alphabet) != 1:
    print("Invalid input Error")
else:
    if alphabet.isupper():
        print(alphabet, "is an uppercase alphabet")

