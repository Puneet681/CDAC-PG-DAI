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
    
    def calculateGPA(self):
        return 0.334*self.__m1+0.5*self.__m2+0.25*self.__m3
    
    def __str__(self):
        return f"student id :- {self.__sid}\nname :-  {self.__name}\nm1 :-{self.__m1}\nm2:- {self.__m2}\nm3 :- {self.__m3}"
    

d = {}
def disp_all():
    for k,v in d.items():
        print("id--->",d[k][0])
        print("name--->",d[k][1])
        print("m1--->",d[k][2])
        print("m2--->",d[k][4])
        print("m3--->",d[k][5])

def add_stu():
    x = int(input("enetr number of students"))
    for i in range(x):
        s = (input("enter value : - student id,name,m1,m2,m3" )).split(',')
        i = Student(s[0],s[1],int(s[2]),int(s[3]),int(s[4]))
        k = i.get_sid()
        d[k] = [i.get_name(),i.get_m1(),i.get_m2(),i.get_m3()]
    return d

def search_by_id():
    sid = input("enetr id of a student")
    k = d.get(sid)
    if k!=None:
        return (sid,k)
    
def search_by_name():
    name = input("enter student name")
    for k,v in d.items():
        if v[0]==name:
            return (k,d[k])

def calculateGPA():
    sid = input("enetr student id")
    v = d[sid]
    obj = Student(sid,v[0],v[1],v[2],v[3])
    return obj.calculateGPA() 