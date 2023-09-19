def add_name(d = dict, name = str , vehicle = str):
    d[name] = vehicle
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
def mod_vic(d = dict, name = str , n_vic = str):
    v = d.get(-1)
    if v != -1:
        ans = input("person name found \nare you sure you want to modify name \n(y/n)")
        if ans =="y":
            d[name]=n_vic
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

def search_have_vic(d = dict, vic = str):
    l = {}
    for k in d:
        if d[k]==vic:
            l.append(k)
    if len(l) == 0:
        return 0 , []
    else:
        return 1 ,  l
    