
end = int(input("Enter the no of months : "))

start = int(input("""
0.monday
1.Tuesday
2.Wednesday
3.Thursday
4.Friday
5.Saturday
6.sunday
Enter the day the month starts with : """))


print('Mon\tTue\tWed\tThu\tFri\tSat\tSun')


for i in range(start,end+1):
    if i <= start:
        print('\t'*start,f"{i}\t",end='')


