a = "this is a cat,cat is cute, where is you r cat? mine is here"
pos = 0

for i in range(len(a)):
    pos = a.find("cat",pos+1)
    if pos != -1:
        print(pos)
    else:
        break

pos = 0
print("*"*50)
for i in range(len(a)):
    pos = a.rfind("cat",0,pos-1)
    if pos==-1:
        break
    print(pos)

pos = 0
print("*"*50)
try:
    for i in range(len(a)):
        pos = a.index("cat",pos+1)
        print(pos)
except:
    pass

pos = 0
print("*"*50)
try:
    for i in range(len(a)):
        pos = a.rindex("cat",0,pos-1)
        print(pos)
except:
    pass
