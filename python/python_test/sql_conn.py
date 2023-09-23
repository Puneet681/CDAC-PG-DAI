import sqlite3 as sqlite

try:    
    conn = sqlite.connect('mydb.db')
    print("Connection Sucessfull")
    
except:
    print("Error Occured")

cursor = conn.cursor()
choice = 0

def displayall():
    cursor.execute('select * from product')
    for row in cursor.fetchall(): # to fetch all rows as list of tuples [(values),(values)]
        name = row[1].ljust(10," ")
        print(f"pid : {row[0]} | pname : {name} | qty : {row[2]} | price : {row[3]}")

def displaybyid(pid):
    try:
    # ? dynamically id is provided - it should be provided as tuple othewise use fstring                                                                                                                         
    # cursor.execute('select * from product where pid={pid}') # <----- anothe way  
        cursor.execute('select * from product where pid=?',(pid,)) 
        row = cursor.fetchone() # to fetch one rows as list of tuples [(values),(values)]
        name = row[1].ljust(10," ")
        print(f"pid : {row[0]} | pname : {name} | qty : {row[2]} | price : {row[3]}")
    except Exception as e:
        print("Error Occured : ",e)
    
def addnewproduct():
    try:
        pid = int(input("Enter pid : "))
        pnm = input("Enter Name : ")
        qty = int(input("Enter qty : "))
        price = float(input("Enter Price : "))
        cursor.execute("insert into product values (?,?,?,?)",(pid,pnm,qty,price))
        conn.commit() # to commit changes to cursor
    except Exception as e:
        print("Wrong Input",e)
        conn.rollback() # to undo cursor made changes 


def delbyid(pid):
    try:
        cursor.execute("delete from product where pid = ? ",(pid,))
        conn.commit() # to commit changes to cursor
        return True
    except Exception as e:
        print("Wrong Input",e)
        conn.rollback() # to undo cursor made changes 
        return False
    
def updatebyid(pid,pname,qty,price):
    try:
        cursor.execute("update product set pname = ?, qty = ?, price = ? where pid = ? ",(pname,qty,price,pid))
        conn.commit() # to commit changes to cursor
        return True
    except Exception as e:
        print("Wrong Input",e)
        conn.rollback() # to undo cursor made changes 
        return False


    
while choice != 6:
    choice = int(input("""
                       1.add new product
                       2.delete product by id
                       3.update product by id
                       4.display all
                       5.display all by id
                       6.exit
                       """))
    match choice:
        case 1:
            addnewproduct()
        case 2:
            pid = int(input("Enter ID: "))
            status = delbyid(pid)
            if status:
                print("Deleted Sucessfully")
            else:
                print("Not Found")
        case 3:
            pid = int(input("Enter ID: "))
            pname = input("Enter New Name : ")
            qty = int(input("Enter New Qty : "))
            price = float(input("Enter New Price : "))
            status = updatebyid(pid,pname,qty,price)
            if status:
                print("Updated Sucessfully")
            else:
                print("Not Found")
                
        case 4:
            displayall()
        case 5:
            pid = int(input("Enter ID : "))
            displaybyid(pid)
            
        case 6:
            print("Thank you for visiting...")
            conn.close() # to release resource 
                     

