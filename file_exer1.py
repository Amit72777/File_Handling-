

f = open("file1.txt",'r')
f2 = open("file2.txt",'a')

for line in f.readlines():
    a,b =line.split(",")
    f2.write(f" {a}'s salary is {b}")

# file1 content 
'''
file1.txt 
harshtit,100
Mohit,50
Aaditya,200
Nitish,500
Rohit,1000

'''

# file2 content 
''' 
file2.txt
 harshtit's salary is 100
 Mohit's salary is 50
 Aaditya's salary is 200
 Nitish's salary is 500
 Rohit's salary is 1000

'''