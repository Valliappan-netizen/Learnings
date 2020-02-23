from collections import Counter
list1 = [1,1,1,2,2,3,3,2,2,1,4,4,3,5,5,4,5]
c = Counter(list1)
print(c)
print(list(c.elements()))
print(list(c.most_common()))
sub = {1:3, 3:2, 2:3, 4:1,5:1}
c.subtract(sub)
print(c.most_common())
letter1 = 'aaabbccabdcceedde'
let = Counter(letter1)
print(let)
print(let.keys())
print(let.values())
print(let.items())
letter2 = 'bbbaaabbcccaaddccdddee'
let1 = Counter(letter2)
print('Intersection is: ',let&let1)
print('union is: ',let|let1)