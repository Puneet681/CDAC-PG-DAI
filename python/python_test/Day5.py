 #-=-=-=-=-=-=-=-=-=-=-=-=-=-= Match Case =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# only available on version 3.10 and above 
'''
choice = int(input("Enter Choice : "))

match choice:
    case 1:
        print("choice is 1 ")
    case 2:
        print("choice is 2 ")
    case 3:
        print("choice is 3 ")

color = input("Enter value ; ")
    case 'red' | 'yellow' :
        print("red or yellow selected")
    case 'green' :
        print('green selected')
    case others:
        print("Default case")
'''

#=-=-=--=-=-=-=-=--=-= Choice using if else =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

choice = input("Enter value ; ")

if choice == 'red' or 'yellow' :
    print("red or yellow selected")
if choice == 'green' :
    print('green selected')
else:
    print("Default case")

#=-=-=-=-=-=-=-=-=-=-=-=-=-= =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=

courselst = [('DBDA',100),('DAI',40)]

choice = int(input("""
1. add new course
2. delete the course
3. modify the course duration
4. modify course name
5. display all
6. display only course with capacity > given capacity
7. exit
"""))
