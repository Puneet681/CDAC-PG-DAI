'''Create user table in databse to store username, address, mobile and email. Add 10 records in the
table
Write a python program to accept username and address from user check whether user exists in
user table. If exists, then display details of user on the screen and if user not found then accept user
details and store it in the table (Use sqlit3)'''

import sqlite3 


try:
    conn = sqlite3.connect('database.db')
    print("Connection Sucessfull....")
except:
    print("Connection failed....")
    
cursor = conn.cursor()

'''for i in range(10):
  cursor.execute("insert into userdata values(?,?,?,?)",(f"user{i}",f"adress{i}",54645409+i, f"email{i}"))
conn.commit()'''
    
def find():
    uname_n = input("enetr user name you want to find")
    address_n = input("enter user address")
    cursor.execute("select * from userdata")
    for row in cursor.fetchall():
        if row[0] == uname_n and row[1] == address_n:
            print("user found")
            print(f"username : {row[0]} | address : {row[1]} | number : {row[2]} | email : {row[3]}")
            break
    
    else:
        print("user not found\nenetr user details :- ")
        uname = input("enetr user name you want to find :- ")
        address = input("enter user address")
        number = int(input("enter number of user :- "))
        email = input("enter user email :- ")
        cursor.execute("insert into userdata values (?,?,?,?)",(uname,address,number,email))
        
        
    
def dispall():
    cursor.execute("select * from userdata")
    for row in cursor.fetchall():
        print(f"username : {row[0]} | address : {row[1]} | number : {row[2]} | email : {row[3]}")
            
    
            


while True :
    case = int(input('''
                     1. find user
                     2. display all users
                     3. Exit
                     '''))
                     
    match case :
        case 1:
            find()
        case 2:
            dispall()
        case 3:
            print("Exiting....")
            conn.close()
            break




