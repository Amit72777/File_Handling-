# we introduce writerows function in CSV module 

from csv import writer 

with open('file4.csv','w',newline = '') as f:
    csv_writer =  writer(f)
    # use writerows 
    csv_writer.writerows([['name','Country','Gender'],['Rahul','India','male'],['lena','Russia','Male']])