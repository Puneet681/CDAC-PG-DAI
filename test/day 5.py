'''

#-=-==-=-=-=-=--=-==-=-=-=-=-=-  SETS  =-=-=-=-=-=-=-=-=-=-=-
#--------- set is unordered , unique , mutable , no duplicates , store immutable data ------

a = 'Ankush'
b = set(a)
print(b)

a = [1,2,3,4]

b = set(a)
print(b)

a = set(['python','pearl','ruby','os','python']) # unordered set will be printed
b = set(a)
print(b)

# ================ functions ====================

s = set("this is set")
print(s)


s = set(["python","perl","python","os"])
print(s)

s = {12,1,2,3,4,58,54,26,84,387,54,300}
s.add(25) #-------------------adds a single unique and im-mutable value if not then it ignore
print(s)

s.update((25,26,24)) #------------------adds multiple values form itrable ignores duplicate and mutable data
print(s)

print(s.pop()) #---------------- removes any random value from the set 

s.remove(300) #----------------- Removes the given value from the set if not found throws an exception
print(s)

s.discard(300) #---------------- removes given value from the set if not found do not throws an exception
print(s)

s = set({12,1,2,3,4,(1,2,3)})
s.add("fhhfhkookpok")
print(s)

#------------------ ser operations ------------------------

'''

s1 = {1,2,3,4}
s2 = {4,5,11,12,13}
print("s1 Union s2",s1 | s2)
print("s1 intersection s2",s1 & s2)
print("s1 Difference s2",s1 - s2)
print("s2 Difference s1",s2 - s1)
print("s1 symmetric diff s2 : ",s2 ^ s1)

print()

print("s1 Union s2",s1.union(s2))
print("s1 intersection s2",s1.intersection(s2))
print("s1 Difference s2",s1.difference(s2))
print("s2 Difference s1",s2.difference(s1))
print("s1 symmetric diff s2 : ",s2.symmetric_difference(s1))
print("s1 symmetric diff s2 : ",s2.symmetric_difference(s1))


s1 = {1,2,3,4}
s2 = {3,4}

print("superset",s1.issuperset(s2),s1>s2)
print("subset",s1.issubset(s2),s1<s2)
print("disset",s1.isdisjoint(s2))

