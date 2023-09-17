choice = int(input('''enter your choice'
1. Accept Data
2. Delete data by value
3. delete data by position
4. sort
5. reverse
6. Print in sorted order without changing original list
7. print in reverse order without changing original list
8. display data
choose : -'''))

'''1. Accept Data
a) add at last position
b) add at given position
2. Delete data by value
display message deleted successfully
or not found
3. delete data by position
a) delete last element
b) delete from particular position
4. sort
a) ascending
b) descending
5. reverse
6. Print in sorted order without changing original list
7. print in reverse order without changing original list
8. display data
a) normal
b) numbered'''

lst = input("enter the list to do oprations")

def add_by_pos(l):
    in_ch = input('''a) add at last position
b) add at given position:- 
''')
    if in_ch == 'a':
        add_at_last(l,val)
    if in_ch == 'b':
        add_at_giv_pos(l,val,pos)
def add_at_last(l,val):
    l.append(val)
    return True
def add_at_giv_pos(l,val,pos):
    l.insert(pos , val)
    return True

def del_by_val(l,val):
    l.remove(val)

def del_(l):
    in_ch = input('''a) delete last element
b) delete from particular position
''')
    if in_ch == 'a':
        del_at_last()
    elif in_ch == 'b':
        del_by_pos()
def del_at_last(l):
    del(l[len(l)])
def del_by_pos(l):
    print([l])
    pos = input("enter position to del")
    del(l[pos])
def soort(l):
    in_ch = input('''a) ascending
b) descending :- 
''')

    if in_ch == 'a':
        soort_acc()
    elif in_ch == 'b':
        soort_dec()
def soort_acc(l):
    l.sorrt()
def soort_dec(l):
    l.soort(reverse = True)

def rev():
    pass

def soort_NC():
    pass

def rev_NC():
    pass

def disp():
    pass
def disp_nor():
    pass
def disp_numbered():
    pass



