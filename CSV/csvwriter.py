
from csv import writer

with open('file4.csv','w',newline = '') as f:
    csv_writer =  writer(f)
    # two method of writeing a file writerow() = take a one list or tuple  , writerows() = take one list but nested with multiple list 
    csv_writer.writerow(['name','Country','Gender'])
    csv_writer.writerow(['Rahul','India','male'])
    csv_writer.writerow(['lena','Russia','Male'])

    