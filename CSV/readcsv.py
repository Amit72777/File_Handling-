from csv import reader
# reader function read a csv file  as a list 
with open("file.csv",'r') as f:
    csv_reader = reader(f)
    next(csv_reader)     #  Use for skip a column name 
    for i in csv_reader:  # CSV reader is a iterator 
        print(i)


'''

Output:- 

['Harshit', 'harshitvashist34@gmail.com', '+919123924474', 'indore']
['Rahul', 'rahulraj234@gmail.com', '+919873456386', 'mahir']
['utkarsh', ' Utkarshdwiv23@outlook.com', '+918376253842', 'Satna']


'''