'''
lst = [10,20,10,34]
lst.append('hello') # appends as single string
print(lst)
print(len(lst))
lst.extend('Testing') # extend append string as seperate character 
print(lst)
print(len(lst))

lst.pop() # pop last element
print(lst)

lst.pop(2) # pop at given index
print(lst)

lst.remove(10) # remove the given val (if not found throws an exception)
print(lst)

if 100 in lst: # it will check if val exist or not , won't tell position like find does
    lst.remove(100)
print(lst)

del(lst[3]) # delete the element at given index
print(lst)

print(len(lst))

print(lst.index('hello')) # give the index of value 

print(lst.clear())

print(lst)

lst.extend([1,2,3,4,5,'hello','a','b','c'])
print(lst)

a = lst.copy() #chnages in one list doesn't reflect in other 
print(a)

a.pop() 
print(a)
print(lst)

b = [5,6,3,7,2,8,4]
b.sort() # sort the list 
print('sorted: ',b)
b.sort(reverse=True)
print('sorted reverse : ',b)

c = [5,4,2,3,1,7,8]
print("normal : ",c)
c.reverse() # only reverse sequence does not sort the array
print("reversed : ",c)

lst = [12,23,34]
# it will copy the reference
# chnage in one list will reflect in other list

lst1 = lst # referenced to same list 
lst2 = lst.copy() # created shallow copy

#=-=-=-=-Shallow and deep copy=-=-=-=-=-

lst.append(100)
print(lst1)
print(lst2)
lst1.append(["hggh", "hsfuihrui"])
print("lst 1 == ",lst1)
lst3 = lst1.copy()
lst3[4].append("test")
print("testing shallow copy")
print("lst1 == ",lst1)
print("lst3 == ",lst3)
print("\n")
import copy

lst4 = copy.deepcopy(lst1)

print("deep copied lst4 = ",lst4)
print("testing deep copy")
lst4[4].append("test2")

print("lst1 == ",lst1)
print("lst4 == ",lst4)

#-=-=-=-=-=-=-=-=-=-=-= Zipping Multiple Lists-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 

lst = [12,1,23]
lst1 = ["pune","mumbai","delhi","kolkatta"]

for val in zip(lst,lst1): #[(12,'Pune'),(1,'mumbai')]
    print(val[0], "---->",val[1])

print()

for x,y in zip(lst,lst1):
    print(x,"---->",y)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-= Enumerate The List =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

for x,y in enumerate(lst): # x --> index , y ---> value 
    print(x,y)

print()
#-=-=-=-=-=-=--=-=-=-=-=-= Sorted and Reversed =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

lst = ['c','b','a']
print(lst)
print(sorted(lst))
print(sorted(lst,reverse = True))
print(reversed(lst))
print(lst)

#-=-=-=-=-=-=-=-=-to find all even number-=-=-=-=-=---=-==-=-=-=-=-=-

lst = [12,1,3,23,14,25,16,20,22,26]

lst1 = []
for num in lst:
    if num%2==0:
        lst1.append(num)
print(lst1)

#=-=-=-=-=-=-=-=-=-=-==-=list comprihensive oprator-=-=--=-=-=-=-=-=-=-=--=-=-=-=

lst1 = [num for num in lst if num%2==0]
print(lst1)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-= FILTER =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#-----------------using lambda---------------

lst1 = [1,2,3,4,54,52,54,56,2,3]
lst2 = list(filter(lambda x:x%2==0,lst1))
print(lst1,"\n",lst2,"\n")

lst3 = list(filter(lambda x:x%2==0 and x>10,lst1))
print(lst1,"\n",lst3,"\n")

#-----------using user defined function-----------

def f1(n):
    n=n+1
    return n%2==0 and n>15

lst4 = list(filter(lambda x:f1(x),lst1))
print(lst1,"\n",lst3,"\n")


#=-=-=-=-==-=-=-=-=-==-=-=-MAP -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

lst1 = [1,2,3,12,13,10]

for num in lst1:
    lst.append(num+10)
print(lst1)

print([num+10 for num in lst1])

#----------------using lambda------------

lst2 = list(map(lambda x : x+10 ,lst1))
print(lst2)


#-------------using User Defined function------------

def f2(n):
    f = 1
    for i in range(2,n+1):
        f = f*i
    return f
    
lst3 = list(map(lambda x:f2(x), lst2))
print(lst3)



#=-=-=-=-=-=-=-=-=-=-=-=-REDUCED=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# reduces the ittrable into a single value using the Expression given
import functools

#------------------------lambda--------------------

lst = ['python','perl','linux','os']
lst2 = [1,2,3,4,5]

s = functools.reduce(lambda acc,s:acc+s if len(acc)>len(s) else s ,lst)
s2 = functools.reduce(lambda x,y:x+y,lst2)
print(s)
print(s2)


s = functools.reduce(lambda acc,s:acc+s[1:3],lst,'') # initail position will be always taken as first val of string 
print(s)

#=-=-=-=-=-=-=-=-=-SORT=-=--=-=-=-=-=-=-=-

lst = [(1,"zzz",45),(0,"bbb",56),(5,"aaaa",46)] 

#------------------lambda-------------------------
lst.sort()
print(lst)
lst.sort(key = lambda x:x[1])
print(lst)

lst.sort(key = lambda x:x[1],reverse=True)
print(lst)


#-=-=-=--=-=-=-=-=-=-=-=- packing and unpacking of tuples -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

num = 1,2,'sdf','ggbb' # packing of tuple 
print(num)

def f1(a,b):
    a = a+10
    b = b+10
    c = a+b
    return a,b,c

data=f1(23,24) # unpacking of tuple
print(data)
x,y,z=f1(23,24)
print(x)

a = 12, #this is tuple not int
print("%d is the number"%(34,))
print(type(a))

def addition(a=2,b=5,c=12,*t): # [ *tuple_name ] add tuple at end to store more vaulues than parameters 
    s = a + b + c
    print(t)
    for n in t:
        s = s + n
    return s

print(addition(1,2,3,4,5,6,7,8,9))

'''





