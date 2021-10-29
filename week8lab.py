import math
# 1. Create a variable that stores first name in all lowercase letters
f_name = "chong" 
# 2. Create a variable that stores last name in all uppercase
l_name = "LEE"
# 3. Printing out Hellow firstname and lastname
print("Hello,",f_name.upper(),l_name.lower(),"")
# 4. Printing out two new lines
print("\n")
print("\n")
# 5. Create a new variable that stores first and last name
name = "chong LEE"
# 6. Slice last name from the variable name 
print(name[slice(0,5)])
# 7. Replaces last name in the varible in step 5 with last name, Walsh college student
print(name[slice(6,9)],", Walsh College Student")
# 8. Printing out the following:
print('"Start by doing what\'s necessary; then do what\'s possible; and suddenly you are doing the impossible - Francis of Assisi"')
# 9. Stores 2 decimal numbers as variables
num1 = 5.5
num2 = 2.5
# 10. Storing one addition, one subtraction, one multiplication, and one divison operation of these variables as variables
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
divison = num1 / num2
# 11. Printing out results of question 10
print(num1,"plus",num2,"equal",addition)
print(num1,"minus",num2,"equal",subtraction)
print(num1,"multiply by",num2,"equal",multiplication)
print(num1,"divided by",num2,"equal",divison)
# 12. Create a new variable call sq_root that stores the square root of the variable that holds the result of the multiplication operation was perform
sq_root = math.sqrt(multiplication)
print("The square root of",multiplication,"equals",sq_root)
# 13. Storing the current month as a string variable and day of the month as a numeric variable
month = "October"
day = 28
# 14. Output variables in question 13 on a new line and tabbed over two times formatted different from question 12
print(f"\n\t\tToday is the day {day} of the month of {month}.")
