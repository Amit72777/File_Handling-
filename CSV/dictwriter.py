from csv import DictWriter

with open('file1.csv','w',newline = '') as f :
    csv_writer = DictWriter(f,fieldnames = ['First_name','Second_name','age'])  # field name use for header
    csv_writer.writeheader()  # header ko write karega 
    # writerrow,writerows

    csv_writer.writerow({'First_name' : 'Ragav' ,  'Second_name' : 'Yadav','age' : 29} ) 
    csv_writer.writerow( {
        'First_name' : 'Rahul',
        'Second_name' : 'Kushwaha',
        'age' : 18
    } )

    csv_writer.writerows([
        {'First_name' : 'Utkarsh','Second_name' : 'Dwivedi','age' : 21} ,
        {'First_name' : 'Navneet','Second_name' : 'Vishwkarma','age' : 19}, 
        {'First_name' : 'Rakhi','Second_name' : 'Pandey','age' : 20} 
        ])

