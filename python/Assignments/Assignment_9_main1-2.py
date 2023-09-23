#A9Q1

class Student:
    def __init__(self,sid='',name='',m1=0,m2=0,m3=0):
        self.__sid = sid
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        
    def set_sid (self,sid):
        self.__sid = sid
    
    def set_name (self , name):
        self.__name = name
    
    def set_m1 (self,m1): 
        self.__m1 = m1
    
    def set_m2 (self,m2):
        self.__m2 = m2
    
    def set_m3(self,m3):
        self.__m3 = m3
    
    def get_sid (self):
        return self.__sid
    
    def get_name (self):
        return self.__name
    
    def get_m1 (self):
        return self.__m1
    
    def get_m2 (self):
        return self.__m2
    
    def get_m3 (self):
        return self.__m3
    
    def __str__(self):
        return f"student id :- {self.__sid}\nname :-  {self.__name}\nm1 :-{self.__m1}\nm2:- {self.__m2}\nm3 :- {self.__m3}"
    
s = Student("123","Puneet",84,85,100)

x = int(input("enetr number of students : "))
d = {}
s.get_sid()
s.get_name()
s.get_m1()
s.get_m2()
s.get_m3()

'''for i in range(x):
    s = (input("enter value : - student id,name,m1,m2,m3" )).split(',')
    i = Student(s[0],s[1],int(s[2]),int(s[3]),int(s[4]))
    k = i.get_sid()
    d[k] = [i.get_name(),i.get_m1(),i.get_m2(),i.get_m3()]'''
    
#print(d)


#A9Q1

import A9_Q2_module as Q2

while True:
    case = int(input('''1. Add student
2. Display All Student
3. Search by id
4. Search by name
5. calculate GPA of a student
6. Exit :- '''))
    
    match case:
        case 1:
            Q2.add_stu()
        case 2:
            print(Q2.disp_all())
        case 3:
            print(Q2.search_by_id())
        case 4:
            print(Q2.search_by_name())
        case 5:
            print(Q2.calculateGPA())
        case 6:
            break




