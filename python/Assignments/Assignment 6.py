# ---------------------- Q1
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red" , 'Yellow' ,'orange']

sampleSet.update(sampleList)
print()


# ---------------------- Q2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection((set2)))

# ---------------------- Q3

set1 = {10, 20, 30, 40, 50,25}
set2 = {30, 40, 50, 60, 70,100}

print(set1.symmetric_difference(set2))

# ---------------------- Q4

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

print(set1.union(set2))

print(set1.difference(set2))

print(set1.symmetric_difference(set2))

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)

print(set1)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.difference_update(set2)

print(set1)

# ------------------- Q5

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

a = 0

for i in set1:
    a = a+i
avg = a//len(set1)

for i in set2:
    if i>avg:
        set1.add(i)
print(set1)

# ----------------- Q6

#Write a program to accept multiple values from user and add it in the set. And display only
#string with length of the strings>n (note: accept value of n from user)


n = int(input("enter the lengeth of string"))

s = input("enter a string")

set1 = set()
while True:
    s = input("enter a string")
    if s == 'q':
        break
    if len(s)>n:
        set1.add(s)

print(set1)    

