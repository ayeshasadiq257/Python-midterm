def my_function(name):
  print(name + " is an islamic country")
my_function("pakistan")
my_function("saudi arabia")
my_function("turkey")

fruits = {"apple", "banana", "cherry"}
print(len(fruits))

tuple = ("banana",)
print(type(tuple))
#NOT a tuple
tuple = (24)
print(type(tuple))

while True:
    name= str(input('enter your name'))
    fatname= str(input('enter your father name'))
    age= str(input('enter your age'))
    cls= str(input('enter your class'))
    rollno= str(input('enter your rollno'))
    course= str(input('enter your course'))
    adrs= str(input('enter your address'))
    if 'ayesha' in name:
        print ('biodata is complete')
    elif 'sadiq' in fatname:
        print ('my father name is sadiq')
    elif '19' in age:
        print ('my age is 19')
    elif 'bano qabil' in cls:
        print ('i study in banoqabil')
    else:
        continue
      
    
    
