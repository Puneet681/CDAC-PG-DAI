def add(x):
    if x ==1:
        return 1
    else:
        return x+add(x-1)

print(add(10))
