
'''
a = "this is a cat,cat is cute, where is you r cat? mine is here"
b = 'cat'
pos = a.rfind(b)
print(pos)

while pos != -1 :
    pos = a.rfind(b,0,pos)
    print(pos)

print(a.count(b))

#a.split()

'''

'''
a = 'aaabbbc, i like cats and dogs, bbbcccaa'
print(a.split(' '))
print(a.split(','))
print(a.strip('abc, '))
print(a.lower())
print(a.upper())
print(a.isupper())
print(a.lstrip('abc, '))
print(a.startswith('like'))
print(a.startswith('aa'))
b = ['ank','ush']
print(' '.join(a))
print(''.join(b))
print("this is this a string".replace('is','xxxxx'))
print("this is this a string".replace('is','xxxxx',1))

print('123.45'.isdigit())
print('123.45'.isdecimal())
print('123.45'.isalnum())
print('123.45'.isnumeric())

print(a.ljust(60,"@"))
print(a.rjust(60,"@"))

'''
'''

# Efficient memory allocation in python - assign same memory address to same value 

a = 10
b = a
c = 10
d = int(input("Enter number input : "))

print(id(a),id(b),id(c),id(d))

x = "hello"
y = x
z = 'hello'
w = input("Enter string input : ")

print(id(x),id(y),id(z),id(w))

'''

#-=--=-=-=-=-=-=-=-=-=-=-list operations-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

a = [1,2,3,4,5,'python','is','fun',[4,3,2,1],True]

print(len(a)) # to find lenght of string
print(a[4])
print(a[8])
print(a[8][1])

for i in a:
    print(i)

s = 'ankush'

for i in s:
    print(i)

a.extend("abcd")
print(a)

a.insert(5,6)
a.insert(6,[11,22,33])

print(a)
















