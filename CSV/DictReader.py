from csv import DictReader
# reader function read a csv file  as a dictionary  
with open("file.csv",'r') as f:
    # csv_reader is a iterator 
    csv_reader = DictReader(f)   
    
    for i in csv_reader:
        print(i)

# Dictreader(f,delimiter = "|") use when csv not a "," seperated they seperate a '|'
        

'''
Output :- 
{'name': 'Harshit', 'email': 'harshitvashist34@gmail.com', 'phone': '+919123924474', 'address': 'indore'}
{'name': 'Rahul', 'email': 'rahulraj234@gmail.com', 'phone': '+919873456386', 'address': 'mahir'}
{'name': 'utkarsh', 'email': ' Utkarshdwiv23@outlook.com', 'phone': '+918376253842', 'address': 'Satna'}

'''