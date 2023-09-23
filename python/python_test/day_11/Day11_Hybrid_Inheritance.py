
# Multiple Inheriatnace and Hybrid Inheritance  

# Hybrid Inheritance

class A:
    def __init__(self,a1=0,a2=0):
        print("In A Constructor ",a1,a2)
        self.__a1 = a1
        self.__a2 = a2
    
    def __str__(self):
        return f"a1 : {self.__a1} a2 : {self.__a2}"
        
    
class B(A):
    def __init__(self,b1=0,**kwarg):
        print("In B Constructor ",b1,kwarg)
        super().__init__(**kwarg) # insted of writing super 
        self.__b1 = b1
    
    def __str__(self):
        return super().__str__() + f"b1 : {self.__b1}"
            

class C(A):
    def __init__(self,c1=0,c2=0,**kwarg):
        print("In C Constructor ",c1,c2,kwarg)
        super().__init__(**kwarg)
        self.__c1 = c1
        self.__c2 = c2
        
    def __str__(self):
        return super().__str__() + f" c1 : {self.__c1} c2 : {self.__c2} "
            
class D(B,C):
    def __init__(self,d1=0,d2=0,**Kwarg):
        print("In D Constructor",d1,d2,Kwarg)
        # Wrong Ways 
        # B.__init__(self,a1=0,a2=0,b1=0)
        # C.__init__(self,a1=0,a2=0,c1=0,c2=0)
        # super().__init__(self,a1=0,a2=0,b1=0,c1=0,c2=0)
        super().__init__(**Kwarg)
        self.__d1 = d1
        self.__d2 = d2
        
    def __str__(self):
        return super().__str__() + f" d1 : {self.__d1} d2 : {self.__d2}"
    
obj = D(a1=12,a2=11,b1=21,c1=31,c2=31,d1=11,d2=14)
print(obj)
print(D.mro()) # Method Resolution Operator
