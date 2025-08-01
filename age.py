"""Write a Python program that asks the user to enter their age and then prints which age group they belong to using if, elif, and else.
Age Groups:
Age 0–12: Child
Age 13–19: Teenager
Age 20–59: Adult
Age 60 and above: Senior"""

age = int(input("Enter your age: "))

if 0>age<=12:
    print("Child")
elif 12<age<=19:
    print("Teenage")
elif 20<=age<=59:
    print("Adult")
elif age>60:
    print("Senior")



