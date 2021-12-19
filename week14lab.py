# Function to get employees ID
def employeeID():
  ID = input("Please enter employees ID: ")

  while True:
    # If the length of ID is 7 characters long break and return data
    if len(ID) == 7:
      break
    # If ID is less than or greater than 7 characters re-enter ID
    elif 7 > len(ID) and len(ID) < 7:
      ID = input("Please Enter a valid ID of 7 digit long: ")
  return ID

#Function to obtain employees Name
def employeeName():
  
  while True:
    # Input employees name
    name = input("Please enter employees Name: ")
    if name == "":
      print("Name cannot be left empty")
    else:
      break
  return(name)

# Function to obtain Email Address
def employeeEA():
  while True:
    email = input("Please enter employees email address: ")
    char_set = {'!','"',"'",'#',"$",'%',"^",'&','*','(',')','=','+',',','<','>','/','?','[',']','{','}','\\','.'}
    # Turning email input into a set of iterable elements separated by a comma
    emailAdd = set(email)
    if email == "":
      print("Email cannot be empty")
    # If the length set of the email contain any of the characters in char_set is greater than zero please re-enter the email
    elif len(emailAdd.intersection(char_set)) > 0:
      print("Email cannot containcharaters: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\., please re-enter Email")
    # Replace @ and _ with no space to comprised for alphanumeric
    elif email.replace("@","").replace("_","").isalnum():
      break
  return(email)

# Function to obtain Address
def employeeAdd():
  while True:
    address = input("Please enter employees Address: ")
    char_set = {'!','"',"'",'#',"$",'%',"^",'&','*','(',')','=','+',',','<','>','/','?','[',']','{','}','\\','.'}
    Add = set(address)
    if address == "":
      print("Address cannot be empty, please try again")
    # If the length set of the email contain any of the characters in char_set is greater than zero please re-enter the address
    elif len(Add.intersection(char_set)) > 0:
      print("Address cannot contain charaters: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\.")
    # Replacing blank space with no space to comprised for alphanumeric
    elif address.replace(" ", "").isalnum():
      break
  return(address)

def employeeSalary():
  while True:
    salary = float(input("Please enter salary: "))
    if salary == 0:
      print("Salary cannot be 0")
    # If salary enter is less than or greater than 27, re-enter salary
    elif 18 > salary and salary < 27:
      print("Salary should be between 18 and 27")
    else:
      break
  return salary

emptylist = []

while True:
  # Calling function 
	ID = employeeID()
	Name = employeeName()
	Email = employeeEA()
	Address = employeeAdd()
	Salary = employeeSalary()

  # Creating the employee information dictionary
	employeeInfo = {
		"ID" : ID,
		"Name (IT Department)" : Name,
		"Email" : Email,
		"Address" : Address,
		"Salary" : Salary * 1.3 # Updating salaries to be 30% higher
	}

  # Appending employeeInfo to info list
	emptylist.append(employeeInfo)

	option = input("Do you want to continue? Y|N: ").lower()
	if option == "n":
		break
print(emptylist)

