
#--------------- Args and Kwargs ---------------------------

def f1 (a = 12, b = 13 , c =14,*tp,**kwargs): # declare args and kwargs 
    print(a,b,c)
    print(tp)
    print(kwargs)
    s = a+b+c
    for i in tp: # to access tuples
        s = s+i
    for k in kwargs.keys(): # to access dictionary 
        s = s+kwargs[k]
    return s
print(f1(1,25,15,684,578,45,x = 45,y=45,z = 843)) # to assign variables 
