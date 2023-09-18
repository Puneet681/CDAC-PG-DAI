def add_name(d = dict):
    name = input("enter name of person")
    vehicle = input("enter vehicle")
    
    d[name] = vehicle
    print(f" new entry added")

def del_name(d = dict):
    name = input("enetr the name you want to delete")
    v = d.get(name,-1)
    if v != -1:
        ans = input(f"are you sure you want to delete {name} (y/n)")
        if ans = "y":
            d.pop(name)
            return 1
        else:
            print("selected no")
            return -1
    else:
        print("value not found")
        return 0
def mod_vic(d = dict
    vic = input("enter the old vehicle name")
    n_vic = input("enter new vehicle name")
    
    for k in d.keys():
        if d[k]==vic:
            ans = input("vehicle name found \nare you sure you want to modify name \n(y/n)")
            if ans =="y":
                d[k]=n_vic
                return 1
            else:
                print("selected no")
                return -1
        else:
            print("value not found")
            return 0
            
                

def search_vic(d = dict):
    name = input("enter the name of person")
    for k in d:
        if k==name:
            return name
        else:
            print("no such veichle name found")
            return 0

def search_have_vic(d = dict):
    vic = input("enter the name of vehicle you want to find")
    new_d = {}
    for k in d:
        if d[k]==vic:
            new_d[k] = vic
        else:
            print("no such veichle name found")
            return 0
    return new_d

def disp_all_ppl(d = dict):
    print([k for k in d.keys()])
    return 1

def disp_all_vic(d = dict)
    print([v for v in d.values()])
    return 1
    