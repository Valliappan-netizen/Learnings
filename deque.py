from collections import deque
list1 = ['one','two','three','four','five']
d = deque(list1)
print(d)
d.appendleft('zero')
print(d)
d.pop()
print(d)
'''
5. index(ele, beg, end) :- This function returns the first index of the value 
mentioned in arguments, starting searching from beg till end index.
'''
print(d.index('three',1,4))

'''
 insert(i, a) :- This function inserts the value mentioned in arguments(a) 
 at index(i) specified in arguments.
'''
d.insert(3,'two.five')
print(d)
print(d.count('one'))


