path = 'classs_assignment_data.txt'
d = {}
d2 = {}
total = 0
with open (path , 'r') as f:
    for line in f:
        line = line.rstrip("\n")
        l = line.split(':')
        k = l[4]
        sal = int(l[3])
        total = total + sal
        v = d.get(k,-1)
        if v == -1:
            s = 0
            d[k] = [sal]
            s = s + sal
            d2[k] = s
        elif v !=-1:
            d[k].append(sal)
            s = s + sal
            d2[k] = s
print(d)
print(d2)
print(total)