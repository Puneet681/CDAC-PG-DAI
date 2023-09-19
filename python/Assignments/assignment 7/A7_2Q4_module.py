def add_name(d = dict , city = None):
    tree = []
    if city == None:
        city = input("enter name of city")
    while True:
       x = input("enter tree \nenter 'q' after list is done")
       if x =='q':
           break
       tree.append(x)
       d[city] = tree 
    return 1

def del_name(d = dict , name = str):
    v = d.get(name,-1)
    if v != -1:
        ans = input(f"are you sure you want to delete {name} (y/n)")
        if ans == "y":
            d.pop(name)
            return 1
        else:
            return -1
    else:
        print("value not found")
        return 0
def mod_vic(d = dict, city = str):
   v = d.get(city , -1)
   if v != -1:
       ans = input("person name found \nare you sure you want to modify name \n(y/n)")
       if ans =="y":
           add_name(d,city)
           return 1
       else:
           return -1
   elif v == -1:
           return 0
          
            
                

def search_vic(d = dict , name = str):
    v = d.get(name, 0)
    if v != -1:
        return v
    return v

def search_have_tree(d = dict, tree = str):
    l = []
    for k in d:
        for i in range(len(d[k])):
            if d[k][i]==tree:
                l.append(k)
    if len(l) == 0:
        return 0 , []
    else:
        return 1 ,  l
    