from collections import ChainMap
dict1 = {'Thirukural' : 'Thiruvalluvar','Ramayanam':'Kamban','Ponnniyin selvan':'Kalki'}
dict2 = {'one':1,'two':2,'three':3}
cm = ChainMap(dict1,dict2)
print(cm.maps)
print(list(cm.keys()))
print(list(cm.values()))
dict3 = {'a':1,'b':2,'c':3}
cm = cm.new_child(dict3)
print(cm)