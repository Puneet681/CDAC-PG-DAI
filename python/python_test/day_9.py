#-=-=-=-=-=-=-=-=-=-=-=-=-         OOPs            =-=-=-=-=-=-=-=-=-=-=

# -- Topics ----------------------
# Encapsulation
# inheritance
# Polymorphism
# abstraction


class Person: # class name starts with Captal Letter - standards 
    count = 0 # static variable - Common variable for all objects 
    def __init__(self,pid=0,pname="",mob=""): # this is a constructor 3 First parameter is always self
    # without self member variable are not accesible 
        print("In person Constructor")
        Person.count = Person.count + 1 # any static variable must be initialized with Class name 
        self.__pid = Person.count # Static Variable is assigned to Member Variable 
        self.__pname = pname
        self.__mobile = mob 
    
    # static function can be called without creating object 
    @staticmethod # Decorator to call static variable as first value (Otherwise consider it as self)
    def myfunction1(val): # this is a static function/method
        print("In Static Function :",val)
    
    #setter method
    def set_pid(self,pid):
        self.__pid = pid
        
    def set_pname(self,pnm):
        self.__pname = pnm
    
    def set_mobile(self,mob):
        self.__mobile = mob
    
    # Getter methods
    def get_pid(self):
        return self.__pid 
        
    def get_pname(self):
        return self.__pname 
    
    def get_mobile(self):
        return self.__mobile
    
    
    def __str__(self):
        print("In person str method")
        return f"Id: {self.__pid} Name: {self.__pname} Mobile: {self.__mobile}"
    
if __name__ == "__main__":
    p1 = Person("Rajan","22222")
    p2 = Person("Atharva","77777")
    #ro print all the members
    print(p1)
    print(p2)
    
    #to retrive only name #accesor/getter
    print(p1.get_pname())

    Person.myfunction1(12) # calling Static Function 
    #to modify only mobile #mutator/setter 
    p1.set_mobile(555555)
    print(p1)