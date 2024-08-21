#Problem statement: Accept average score from the student of his exam and print his result as follows
# 0 - 49 is Fail
# 50 - 74 is Second Class
# 75 - 90 is First Class
# 91 - 100 is Distinction
# Also check for invalid score

average_score = float(input("Enter students average score:"))

if average_score in range(91,101):
    print("Students results is :Distinction")
elif average_score in range(75,91):
    print("Students results is: First Class")
elif average_score in range(50,75):
    print("Students results is: Second Class")
elif average_score in range(0,50):
    print("Students results is: Fail")
else:
        exit("INVALID INPUT!!")
  
