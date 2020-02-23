from collections import OrderedDict
d = OrderedDict();
d[1] = 'ram'
d[2]='janu'
d[3]='ravi'
d[4]='vicky'
d[5]='venkat'
d[6]='venu'

print(d)

for keys, values in d.items():
    print(keys,values)