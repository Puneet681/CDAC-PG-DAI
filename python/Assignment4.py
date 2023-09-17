#Q1)

c = int(input('enter the count of the days in a month'))
day = int(input('choice\n0 == MONDAY\n1 == TUESDAY\n2 = WEDNESDAY\n3 = THRUSDAY\n4 = FRIDAY\n5 = SATURDAY\n6 = SUNDAY\n'))

date = []

if c==31 or c==30 or c==28:
    for i in range(1,day):
        date.append(str(0))
    
    for i in range(0,c+1):
        date.append(i)

s = 0
end = 7

day_name = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
for i in day_name:
    print(i+" ",end=" ")
print()
for i in range(len(date)):
    for j in range(s,end):
        print(str(date[j]).rjust(3," ") ," ", end = "")
    print()
    s = end
    end = end+7
    if end>len(date):
        end=len(date)
        if int(date[j])==c:
            break


#Q2)
'''

def histogram(h):
    for i in h:
        print("*"*i)

histogram([4,9,7])
'''

#Q3)
'''
lst = ["Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamedunder it as a tired nude Maori", "Rise to vote sir", "Dammit, I'm mad!"]
temp=[]

for str in lst:
    ref = str
    str = str.upper()
    str = str.strip(" '.?!")
    if (" " in str)== True:
        str = str.replace(" ","")
    if ("'" in str)== True:
        str = str.replace("'","")
    if ("," in str)== True:
        str = str.replace(",","")
    if ("?" in str)== True:
        str = str.replace("?","")

    temp.extend(str)
    temp.reverse()
    
    str2="".join(temp)
    temp.clear()
    if str2==str:
        print(f"{ref} \nis palindrome")
    print()
'''

#Q4)

'''
a = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x', 'y' ,'z']

a = 'The quick brown fox, jumps over the lazy dog!!!!'
k = []
for i in a:
    k.append(i.lower())
c = 0
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in a:
    if i in k:
        c = c + 1
    else:
        pass

if c == 26:
    print("Given Sentence is a Panagram")
else:
    print("Given Sentence is not a Panagram")
'''

#Q5)
'''
s = "this is fun"
def f1(s):
    temp = []
    v = ["a","e","i","o","u"," "]
    temp.extend(s)
    for i in range(0, len(temp)):
        if temp[i] not in v:
            char = temp[i]+"0"+temp[i]
            temp[i] = char
    print(temp)

    return  "".join(temp)

    
print(f"rövarspråket of {s} is {f1(s)}")
'''

#Q6)
'''
def fac(x):
    if x == 0:
        return 1
    else:
        return x*fac(x-1)
def main():
    for i in range(1,21):
        print(f"{i} = {fac(i)})")
main()
'''

#Q7)

def sum1(x):
    if x> 1:
        return x+sum1(x-1)
    elif x ==1:
        return x

def main(n):
    for i in range(1,n+1):
        print(i, sum1(i))

n = int(input())

if n <= 0:
    print("Write a number greater than 0 : ")
else:
    main(n)
#Q7)

