# Collection in Python
from collections import namedtuple
#key = namedtuple('Book','name,author,price')
key = namedtuple('Book',['name','author','price'])
value = key('Two states','chetan bhagat',200)
Value1 = key._make(['Half girl friend','chetan bhagat',150]) #assigning value to namedtuple 
print('Refer the named tuple',Value1)
print(Value1[1]);#get value by index
print(value.name)#get value by fields
print(getattr(value,'author')) #we can get value using attributr
print(value._asdict()) #to convert namedtuple to dict
#dict1 = {'Thirukural' : 'Thiruvalluvar','Ramayanam':'Kamban','Ponnniyin selvan':'Kalki'}
#print(key(**dict1))
li = ['Thirukural','Thiruvalluvar',50]
print(key._make(li)) #convert list to namedtuple
print('all the fileds of book: ',key._fields)# to get all the fileds in book tuple
print('Replace book by another book: ',value._replace(name = 'Revolution 2020')) #replace value for a field