
# Multiple Inheriatnace and Hybrid Inheritance  

# Multiple Inheritance
    

class B:
    def __init__(self,b1=0,**kwarg):
        print("In B Constructor ",b1,kwarg)
        super().__init__(**kwarg)
        self.__b1 = b1
    
    def __str__(self):
        return  f"b1 : {self.__b1}"
            

class C:
    def __init__(self,c1=0,c2=0,**kwarg):
        print("In C Constructor ",c1,c2,kwarg)
        super().__init__(**kwarg)
        self.__c1 = c1
        self.__c2 = c2
        
    def __str__(self):
        return  f" c1 : {self.__c1} c2 : {self.__c2} "

class E:
    def __init__(self,e1=0,e2=0,**kwarg):   
        print("In E Constructor",e1,e2,kwarg)
        super().__init__(**kwarg)
        self.__e1 = e1
        self.__e2 = e2
        
    def __str__(self):
        return f" e1 : {self.__c1} e2 : {self.__e2} "
            
class D(B,C,E):
    def __init__(self,d1=0,d2=0,**kwarg):
        print("In D Constructor",d1,d2,kwarg)
        # Wrong Ways 
        # B.__init__(self,a1=0,a2=0,b1=0)
        # C.__init__(self,a1=0,a2=0,c1=0,c2=0)
        # super().__init__(self,a1=0,a2=0,b1=0,c1=0,c2=0)
        super().__init__(**kwarg)
        self.__d1 = d1
        self.__d2 = d2
        
    def __str__(self):
        return super().__str__() + f" d1 : {self.__d1} d2 : {self.__d2}"
    
obj = D(c1=21,c2=31,b1=31,d1=11,d2=14,e1=13,e2=15)
print(obj)
print(D.mro()) # Method Resolution Operator
