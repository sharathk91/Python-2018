import re   #import regular expressions
text = input("Enter the Password to validate: ") #take input password string from user
flag = 0  #assign flag to zero
while True: #loop until the value is false
    if (len(text) < 6): #check if the length of password is less than 6 chars
        flag = -1
        print("Password size should be greater than 6")
        break
    elif (len(text) > 16): #check if the length of password file is greater than 6 characters
        flag = -1
        print("Password size should be lesser than or equal to 16")
        break
    elif not re.search("[a-z]", text):  #check if the password contains lower case letter
        flag = -1
        print("password should have atleast one lower case letter")
        break
    elif not re.search("[A-Z]", text): #check if password contains atleast one upper case letter
        flag = -1
        print("password should have atleast one upper case letter")
        break
    elif not re.search("[0-9]", text): #check if password contains atleast one digit
        flag = -1
        print("password should have atleast one digit")
        break
    elif not re.search("[*!@$]", text):  #check if password contains atleast one special char
        flag = -1
        print("password should have atleast one special character")
        break
    else:      #if above one is not true, then it is a valid password
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Invalid Password")