
#id,name,lastname,hobbies,mobno,email,bdate,address

class Student:
    def __init__(self,sid='',name='',lname='',hobbies=[],mob_no='',email='',bdate='',address=''):
        self.__sid = sid
        self.__name = name
        self.__lname = lname 
        self.__hobbies = hobbies 
        self.__mob_no = mob_no
        self.__email = email
        self.__bdate = bdate
        self.__address = address
        
    def set_sid (self,sid):
        self.__sid = sid
    
    def set_name (self , name):
        self.__name = name
    
    def set_lname (self,lname): 
        self.__lname = lname
    
    def set_hobbies (self,hobbies):
        self.__hobbies = hobbies
    
    def set_mob_no(self,mob_no):
        self.__mob_no = mob_no
    
    def set_email(self,email):
        self.__email = email
    
    def set_bdate(self,bdate):
        self.__bdate = bdate
    
    def set_address(self,address):
        self.__address = address
    
    def get_sid (self):
        return self.__sid
    
    def get_name (self):
        return self.__name
    
    def get_lname (self):
        return self.__lname
    
    def get_hobbies (self):
        return self.__hobbies
    
    def get_mob_no (self):
        return self.__mob_no
    
    def get_email (self):
        return self.__email
    
    def get_bdate (self):
        return self.__bdate
    
    def get_address (self):
        return self.__address
    
    def __str__ (self):
        return f'''sid :- {self.__sid}
        name :- {self.__name}
        last name :-{self.__lname}
        hobbies :- {self.__hobbies}
        mob_no :- {self.__mob_no}
        email :- {self.__email}
        D_O_B :- {self.__bdate}
        address :- {self.__address}
    '''