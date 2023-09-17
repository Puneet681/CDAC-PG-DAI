s = input("enter a string")
x = input("enter a substring too be found")

pos = s.find(x)
print(pos)
while pos !=-1:
    pos = s.find(x,pos+1)
    print(pos)
print(s.count(x))
