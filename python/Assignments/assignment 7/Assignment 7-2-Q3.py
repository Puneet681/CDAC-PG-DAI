'''Write a menu driven program to practice Dictionary functions.
Write a program to accept name of a person and their vehicle and store it in a dictionary.
Ask user if they want to continue to accept multiple values.
Display following menu:
1. Add new person name and a vehicle name.
2. Delete a person name and vehicle name from the dictionary.
----Accept person name from user.
----Check whether person name exists in the dictionary.
----If exists show person name and vehicle name to the user.
----Confirm for deletion, if user enters y
then delete otherwise no. Display appropriate message.
3. Modify vehicle name for the person
----Accept a person name from user.
----Check whether the person’s name exists.
----If the name exists, show the person’s name and vehicle name to user.
Ask for new value and then overwrite the old value.
4. Search vehicle for the given person’s name.
5. Search list of people, who have given a vehicle
6. Display all person names.
7. Display all vehicle names.
8 Exit'''

import A7_2Q3_module as a

dic = {}
name = input("enter Person name\n enter done")
vehicle = input("enter vehicle name")
a.add_name(dic,name,vehicle)



while True:
        
    case = int(input('''
              1. Add new person name and a vehicle name.
              2. Delete a person name and vehicle name from the dictionary.
              3. Modify vehicle name for the person
              4. Search vehicle for the given person’s name.
              5. Search list of people, who have given a vehicle
              6. Display all person names.
              7. Display all vehicle names.
              8 Exit'''))
    
    match case :
        case 1 :
            name = input("enter name of person")
            vehicle = input("enter vehicle")
            status = a.add_name(dic, name , vehicle)
            if status == 1:
                print(" new entry added")
        case 2:
            name = input("enetr the name you want to delete")
            status = a.del_name(dic, name)
            if status == 1 :
                print(f"{name} Deleted from dict = {dic}")
            elif status == -1:
                print("selected no")
            elif status ==0:
                print("value not found")
        case 3:
            vic = input("enter the old vehicle name")
            n_vic = input("enter new vehicle name")
            status = a.mod_vic(dic ,name , n_vic)
            if status == 1 :
                print(f"{name}'s veichle name modified to {n_vic} in dict = {dic}")
            elif status == -1:
                print("selected no")
            elif status ==0:
                print("value not found")
        case 4:
            name = input("enter the name of person")
            status = a.search_vic(dic,name)
            if status != 0: 
                print(f"# {status}  # is the veichle of {name}")
            else:
                print("no such person exists")
        case 5:
            vic = input("enter the name of vehicle you want to find")
            status , l = a.search_have_vic(dic , vic)
            if status == 0:
                print("no such veichle name found")
            else :
                print(f"following is the list of people having vehicle <{vic}>: - \n {l}")
        case 6:
            print("list to all peoples :- ",[k for k in dic.keys()])
        case 7:
            print("list to all peoples :- ", [dic[k] for k in dic.keys()])
        case 8:
            break
    
