#=-=-=-=-=-=-=-=-=-=-=-=-=-=-    DAY 7    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#------------------------- File Handling --------------------------------------

# --------------- reading data from file and storing it in list ---------------

path = "day_7_test_file.txt" # should be absolute path of the file (/home/dai/Desktop/day_7_test_file.txt)
l = []
fh = open(path) # pointer fh points towards the file (by default read mode )
for line in fh: 
    line = line.rstrip("\n") # txt file has \n by default to remove it we use str.rstrip(val)
    print(line)
    l.append(line)
    
# --------------------- 

copy_path = 'day_7_test_copy_file.txt' # file to copy/write data 
fh = open(path,'r') # file read mode 
fh1 = open(copy_path,'w') # file write mode 
for line in fh1: 
    fh1.write(line)
fh.close()
fh1.close()


# ------------------

import re 
copy_path = 'day_7_test_copy_file.txt' # file to copy/write data 
fh = open(path,'r') # file read mode 
fh1 = open(copy_path,'w') # file write mode 
for line in fh: 
    lst = line.split(":")
    if lst[2]=="game":
        fh1.write(line)
fh.close()
fh1.close()
# ------------------
# Read/Write specific line using custom condition 
with open (path,'r') as fh:
    with open(copy_path,'w') as fh1:
        for line in fh:
            lst = line.split(":")
            if lst[2] == "game":
                fh1.write(line)
                
                
# ------------------
# Read/Write specific line using RegEx  
import re
with open (path,'r') as fh:
    with open(copy_path,'w') as fh1:
        for line in fh:
            m = re.search("game",line)
            if m != None:
                fh1.write(line)

# ---------------- Summation of Employee Salary ----------------
                
s = 0 
with open (path,'r') as fh:
    with open(copy_path,'w') as fh1:
        for line in fh:
            lst = line.split(":")
            s = s + int(lst[4])
print("Total amount spent =",s)           

fh = open(path,'r')
lst = fh.readlines() # read all line and return a list 
print(lst)
fh.close()

fh = open(path,'r')
s = fh.read(7) # read given no of characters (here will read 7 )
# if we write fh.read() it will read entire file and store it as a string 
print(fh.tell())  # it tells the current cursor/handle position in list 
# fh.seek()  # to move current handle position 
fh.seek(fh.tell()+5) # will read character before and after than (given character) depending on condition  
print(s)

fh.close ()