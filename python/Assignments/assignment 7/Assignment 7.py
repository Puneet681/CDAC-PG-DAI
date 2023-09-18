# ------------------ Q1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

d = {}
for i in range(len(values)):
    d[keys[i]] = values[i]

print(d)


# ------------------ Q2

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)
print({**dict1,**dict2})

# ------------------ Q3

sampleDict = {
"class":{
"student":{
"name":"Mike",
"marks":{
"physics":70,
"history":80
}
}
}
}

val = sampleDict["class"]["student"]["marks"]["history"]
print(val)


# ------------------ Q4

sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"

}

#keysToRemove = ["name", "salary"]

sampleDict.pop('name')
sampleDict.pop('salary')

print(sampleDict)

# -------------------- Q5

sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200}

for k,v in sampleDict.items():
    if v==200:
        print(f"{k}------->{v}")
        
# -------------------- Q6

sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}

sampleDict["location"] = sampleDict['city']

sampleDict.pop("city")

print(sampleDict) 

# -------------------- Q7

sampleDict = {
'Physics': 82,
'Math': 65,
'history': 75
}

temp = 0
x = 0
for k,ArithmeticErrorv in sampleDict.items():
    if int(sampleDict[k]) > temp:
        temp = sampleDict[k]
        x = k
print(x)


# ----------------- Q8

sampleDict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}

x = input("enter employe name")
sal = int(input("enetr new salary"))

for k,v in sampleDict.items():
    if v['name'] == x:
        if v['salary'] < sal:
            v['salary'] = sal
            print("salary has benn modified")
        else:
            print("wrong salary is entered")
print(sampleDict)    
    
    



