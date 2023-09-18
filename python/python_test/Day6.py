
# ------------------Dictionary ------------------
# {"key":value(tuple in following case)}


dec = {'DBDA':(100,50)}

dec['DAI']=(200,50) # add value 
print(dec)

print(dec['DAI']) # Access value using key

dec['DAI']=(100,40) # modify existing value if key alreday exists 
print(dec)

v = dec.get('DAC') # check if key exists or not if not exist return None

if v == None:  
    dec['DAC'] = (100,5)
else:
    x = input("Do yo want to Override [y/n]:  ")
    if x == 'y':
        dec['DAC'] = (100,5)
        
print(dec)


dec = {'DBDA':(100,50)}

v = dec.setdefault("DAC",(100,20)) # check if value exists if not add if yes update 
print(v)
print(dec)



dec = {'DBDA':(100,50),'DAC':(200,5)}
for k in dec: # retrive key and value using keys in loop
    print(k,"--->",dec[k])

dec = {'DBDA':(100,50),'DAC':(200,5)}
for k,v in dec.items(): # retrive key and value using dic.temps() in loop
    print(k,"--->",v)

dec = {'DBDA':(100,50),'DAC':(200,5)}
for k,v in dec.items():
    print(k.ljust(6," "),"--->",v)



#------------------- FUNCTIONS ---------------------

# to add new k:v pair
# if key not their it will add else it will overwrite

d = {"DBDA": {100,60},"DAI":(200,50)}
print(d)

d["DAC"] = (230,50)
print(d)

d1 = {"length": len(d)}
print(d1)

d["DAC"] = (20,50)
print(d)

d1 = {(1,2):"xxxx",(3,4):"ttt"}
print(d1)

# d.get() --> to check if wether key is present
# returns value if key is found if not then returns None / Default value 

v = d.get("DBDA") # without default value 
if v == None:
    print("not found")
else :
    print("key and value found = ",v)
    
    
v = d.get("DBDA111",-1) # with default value 
if v == -1:
    print("not found")
else :
    print("key and value found = ",v)

# with setdefault function
# if value is found will return the value at key 
# if not found it will add k:v pair in dict

v = d.setdefault("DBDA111",10000) # with default value 
if v == -1:
    print(f"{v} is added in dic = \n{d}")
    
else :
    print("key and value found = ",v)
    
# to navigate through the dict

for k in d.keys():
    print(f"{k} ----> {d[k]}")
    
for k,v in d.items():
    print(f"{k} ------> {v}")
    

# Navigate w.r.t. particular condition

d = {"DBDA":(100,52),"DAI":(200,60)}


for k in d.keys(): # iterate keys through dict  
    if d[k][1]>50:
        print(f"{k} ----> {d[k]}")
        

for k,v in d.items(): # iterate keys,values through dict  
    if v[1]>50:
        print(f"{k} ----> {d[k]}")

print(d.values()) # iterate through whole dictionary 
lst = list(d.values()) # iterated and stored in list 
        
# to deletes values
# pop() remove element w.r.t. key value if not found return default value 

v = d.pop("DBDA",-1) 
if v ==-1:
    print("not found")
else:
    print("deleted")
    print(v,d)
    
    
data = d.popitem() # deletes last element 
print(data)

# to make new k:v pair using list
# using formkeys()
k_list = [1,2,3,"gjg",(1,5)]

d3 = dict.fromkeys(k_list)

print(d3)


d4 = dict.fromkeys(k_list,"test")

print(d4)

d1 = {"a":1,"b":3}
d2 = {"a":2,"c":3}
# same key value will be updated and stored in new dict
d5 = {**d1,**d2}

print(d5)

# same key will be updated and d1 will be overwritten by d2
d1.update(d2)
print(d1)

# to make shallow copy

d6 = d5
print(d5)
print(d6)

# to del all k:v pairs

d6.clear()
print(d6)
