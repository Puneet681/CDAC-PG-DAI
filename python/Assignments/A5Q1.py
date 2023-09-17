n = input("""
a.Display Characters at even positions
b.Display Characters at odd positions
c.Display Lenght of String
d.Add 'a' at end of string
e.exit 
""")

s = "this is a prictice program"
k = []
k.extend(s)


if n == 'a':
    lt1 = "".join([k[i] for i in range(len(k)) if i%2 == 0])
    print(lt1)
elif n == 'b':
    lt1 = "".join([k[i] for i in range(len(k)) if i%2 != 0])
    print(lt1)
elif n == 'c':
    print("Lenght of the string is : ",len(s))
elif n == 'd':
    print((''.join(k))+"a"*len(s))
else:
    print("Thank you for Visting !")
    
#print(ltr)
