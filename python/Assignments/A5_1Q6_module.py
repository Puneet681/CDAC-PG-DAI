a = set()
b = set()

def delset(x): # 1.
    if x == 'a':
        x = input("Enter the value to be deleted : ")
        a.remove(x)
        
    else:
        x = input("Enter the value to be deleted : ")
        b.remove(x)
        

def addele(): # 2.
    print("Set Created Sucessfully...")
    y = int(input("How many Enteries you want in second set : "))
    for i in range(y):
        x = input("Enter Input : ")
        a.add(x)

def union(): # 4.
    x = a.union(b)
    print(x)

def createset():
    print("Second Set Created Sucessfully...")
    y = int(input("How many Enteries you want in second set : "))
    for i in range(y):
        x = input("Enter Input : ")
        b.add(x)

def intersect(): # 5.
    x = a.intersection(b)
    print(x)

def difference(): #6.
    x = a.difference(b)
    print(x)

def frozenset(): # 7.
    
    pass
