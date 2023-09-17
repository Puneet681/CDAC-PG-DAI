


#----------- Q6

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]

list2 = [i for i in list1 if i!=""]
print(list2)

#----------- Q 7
'''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

print()

#-------- Q 8

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend('hij')
print(list1)

print()


#----------- Q 9

list2 = [5, 10, 15, 20, 25, 50, 20,20]

a = int(input("Enter no to be found : "))
i = list2.index(a)
print(i)


list2[i] = 200
print(list2)
# -----------OR-----------
for x,y in enumerate(list2):
    if y == a:
        print(x)
        break
        

#--------------Q 10

list2 = [5, 10, 15, 20, 25, 50, 20,20]
a = int(input("Enter no to be removed : "))
for x,y in enumerate(list2):
        if y == a:
            list2.remove(y)
        
print(list2)
'''
