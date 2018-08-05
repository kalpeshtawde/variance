#define variable
number_1=1
number_2=2

#define list
list_1=[number_1,number_2,2,3,'a','b','c',[1,2,3]]

print("Addition of two numbers " + str(number_1 + number_2))

print(list_1[4])

#define dictionary
dict_1={'name':'Trupti', 'age':28}

list_2=[{'name':'Trupti', 'age':28}, {'name':'Kalpesh', 'age':30}]

print(list_2[1]['age'])


#For loop
for val in list_1:
    print("Printing " + str(val))

print("{2}{0}{1}{0}".format("Trupti", "Kalpesh", "Rohit"))