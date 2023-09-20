import re
import sys
def A8Q1():
    '''1. write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
example myemail@google.com o/p myemail'''
    import re
    s = 'myemail@google.com'
    myreg = re.compile("\w*@",re.I|re.M)
    m = myreg.search(s)
    if m !=None:
        print(m.group())
def A8Q2():
    '''Accept lines from user and display only the lines that start with a number or any 2 alphabets'''
    while True:
        x = input('enter a string or "q" to exit : -    ')
        if x == 'q':
            break
        myreg = re.compile("^[a-zA-Z]{2,}|^\d\w*")
        m = myreg.match(x)
        if m !=None:
            print(m.group(),"   ",x)
        else:
            print("unkown character found")
    
def A8Q3():
    '''Write a python program to accept mobile number and validate it. it should contain exactly
10 digits.'''
    mob = input("enter mob. number")

    m = re.search("^[987]\d{9}$", mob)
    if m != None:
        print(" mobile no. is valid")
    else:
        print("not found")
def A8Q4(user_name = '0', password = ""):
    
    data ={}
    '''Write a python program to accept user name and password and validate it. username
should contain only alphabets or digits and password length should be 8, starts with
alphabet and should contain at least one special character(#,@) .
accept username and password from user and validate it. if it is valid then display message
welcome to our application. otherwise ask to re-enter.
(allows maximum 3 attempts to accept password'''

 

    if user_name == '0':
       user_name = input("enter user name")
    if user_name != '0':
        pass
#--------------------------------------------------------------------------------    
    
    m = re.match("[a-zA-Z0-9]{1,}", user_name)
     
    if m == None:
        print("enterd username is not in correct format")
        A8Q4()
        
#--------------------------------------------------------------------------------    
    password = input ('''password length should be 8, starts with
     alphabet and should contain at least one special character(#,@) .''')

    m_pass = re.search("^[a-zA-Z][a-zA-Z0-9_\W]{7,}",password)
    if m_pass == None:
        print("Passward is not in correct format")
        print('''password length should be 8, starts with
        alphabet and should contain at least one special character(#,@) .''')
        A8Q4(user_name)
        
#===============================================================================
    
    case = int(input("1. log in\n2. sign up"))
    match case:
        case 1:
            while True:
                
                user_name_E = input("Enter your username")
                if user_name_E ==  user_name:
                    break
            for i in range(3):
                password_E = input("Enter your password")
                if password_E == password:
                    print("You have sucessfully logged in")
                    sys.exit()
                    
            print("your account is locked for 24 hours\nyou have Enterd wrong password 3 times")
        case 2:
            A8Q4()
                
A8Q4()