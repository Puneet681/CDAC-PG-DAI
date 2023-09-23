import A9_Q2_hobbies_module as Q2

while True:
    case = int(input('''
1. Add Student 
2. Display All Friend
3. Search by id
4. Search by name
5. Display all friend with a particular hobby
6. Exit :- '''))
    
    match case:
        case 1:
            Q2.add_stud()
        case 2:
            print(Q2.disp_all())
        case 3:
            print(Q2.search_by_id())
        case 4:
            print(Q2.search_by_name())
        case 5:
            print(Q2.Hobbies())
        case 6:
            break