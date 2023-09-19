'''Write a program to display following menu and do the following:
1. Add new city and trees commonly found in the city.
2. Display all cities and the list of trees for all cities.
3. Display list of trees of a particular city.
---- Accept a city from user search city and if found display list of trees otherwise
---- Display message not found
4. Display cities which have the given tree.
---- Accept a tree name from user and display all cities in which the tree is found.
5. Delete city
---- Accept city from user and delete the city if found.
---- Prompt user before deletion
6. Modify tree list
---- Accept city and trees to be added in the city. if city exist add trees at the end
of the list
---- Otherwise add city and list
7. Exit'''

import A7_2Q4_module as a

dic = {}
status = a.add_name(dic)
if status == 1:
    print(" 1st entry added")



while True:
        
    case = int(input('''
              1. Add new city and trees commonly found in the city.
              2. Display all cities and the list of trees for all cities.
              3. Display list of trees of a particular city.
              4. Display cities which have the given tree.
              5. Delete city
              6. Modify tree list
              7. Exit'''))
    
    match case :
        case 1 :
            status = a.add_name(dic)
            if status == 1:
                print(" new entry added")
        case 2 :
            print(dic)
            
        case 3 :
            city = input("enter name of city")
            print(dic[city])
        
        case 4:
            tree = input("enter name of tree")
            status , l = a.search_have_tree(dic , tree)            
            if status == 0:
                print("no such veichle name found")
            else :
                print(f"following is the list of city having tree <{tree}>: - \n {l}")
                
        case 5:
            city = input("enter name of city")
            status = a.del_name(dic , city)
            if status == 1 :
                print(f"{city} Deleted from dict = {dic}")
            elif status == -1:
                print("selected no")
            elif status ==0:
                print("value not found")
                
        case 6:
            city = input("enter name of city")
            status = a.mod_vic(dic , city)
            if status == 1 :
                print(f"{city}'s tree list is modified to {dic[city]} in dict = {dic}")
            elif status == -1:
                print("selected no")
            elif status ==0:
                print("value not found")
        case 7:
            break
    

