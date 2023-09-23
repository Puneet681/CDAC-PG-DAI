import re
import sys

def signup(user_name = '0', password = ""):
    
    '''Write a python program to accept user name and password and validate it. username
should contain only alphabets or digits and password length should be 8, starts with
alphabet and should contain at least one special character(#,@) .
accept username and password from user and validate it. if it is valid then display message
welcome to our application. otherwise ask to re-enter.
(allows maximum 3 attempts to accept password'''

 

    if user_name == '0':
       user_name = input("enter user name\n")
       with open("database_login.txt",'r') as h:
           for lines in h:
               m = re.match(user_name,lines,flags=re.I|re.M)
               if m != None:
                   print('Username already Exists...Try Again')
                   
                   return 0
            
    if user_name != '0':
        pass
#--------------------------------------------------------------------------------    
    
    m = re.match("[a-zA-Z0-9]{1,}", user_name)
     
    if m == None:
        print("enterd username is not in correct format")
        signup()
        
#--------------------------------------------------------------------------------    
    password = input ('''password length should be 8, starts with
     alphabet and should contain at least one special character(#,@) .\n''')

    m_pass = re.search("^[a-zA-Z][a-zA-Z0-9_\W]{7,}",password)
    if m_pass == None:
        print("Passward is not in correct format")
        print('''password length should be 8, starts with
        alphabet and should contain at least one special character(#,@) .''')
        signup(user_name)
    
    f = open("database_login.txt",'a')
    f.write(user_name+":"+password+"\n")
    f.close()
        
#===============================================================================
def login() :
    while True:
        
        user_name_E = input("Enter your username\n")
        f = open("database_login.txt",'r')
        for lines in f:
            lines.rstrip("\n")
            m = re.match(user_name_E,lines)
            if m != None:
                lst = lines.split(":")
                user_name = lst[0]
                password = lst[1]
        f.close()
        if user_name_E ==  user_name:
            break
    for i in range(3):
        password_E = input("Enter your password\n")
        print(password_E == password)
        print(type(password_E) , type(password))
        for i in [password , password_E]:
            ordd=[]
            for j in i:
                ordd.append(ord(j))
            print(ordd)
        if password_E == password:
            print("You have sucessfully logged in")
            sys.exit()
            
    print("your account is locked for 24 hours\nyou have Enterd wrong password 3 times")
                
def login_signup():
    while True:
        case = int(input("1. log in\n2. sign up\n3. Exit :- "))
        match case:
            case 1:
                login()
            case 2:
                signup()
            case 3:
                sys.exit()
login_signup()