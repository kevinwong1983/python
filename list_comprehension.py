import unittest
tc = unittest.TestCase()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

employees = {'Alice': 100000, 
             'Bob': 99817,
             'Carol': 122908,
             'Franl': 88123,
             'Eve': 93121}

top_earners = []
for key, value in employees.items():
    if value >= 100000:
        top_earners.append({key, value})
    
print(top_earners)

# list complehention
# [expression + context]
top_earners_list_comp = [{key, value} for key, value in employees.items() if value >= 100000]
tc.assertEqual(top_earners, top_earners_list_comp)

print([x ** 2 for x in range(10) if x%2>0])
print([x.lower() for x in ['I', 'AM', 'NOT', 'SHOUTING']])

# given a multiline string, creat a list of lists - each consiting of all the words in a line that have more than three characters.
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - havin
little or no money in my purse, and nothing particular to intrest me
on shor, I thought I would sail abou t alittle and see the watery part
of the world. It is a way I have of draving off the spleen, and regualting
the curculation. - Moby Dick'''

# all the words in a line 
l = [x for x in text.split('\n')]
tc.assertEqual(len(l), 6)

l = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]
print(l)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

filename = 'list_comprehension.py' # this code

f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())
    
# print(lines)
"""
['filename = 'test_cards.py' # this code',
'',
'f = open(filename)',
'lines = []',
'for lines in f:',
'lines.append(line.strip())'
'',
'print(lines)']
"""

lines2 = [line.strip() for line in open(filename)] # ref count of file becomes zero, file will close (and flused)
tc.assertEqual(lines, lines2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# lamda: simple function with a return object value to its calling environment

# lambda arguments : return expression
tc.assertTrue('42' in 'The answer is 42.')

txt = ['lambda functions are anonymous functions.', 'anonymous functions dont have a name.', 'functions are objects in Python']
a = [str for str in txt if 'anonymous' in str]
print(a)

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt) # make a tuple (bool, string), with bool if anonymous is in string
print(list(mark)) # need cast the map to a list.

a = [(True, str) if 'anonymous' in str else (False, str) for str in txt ]
print(a)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
s = 'Eat more fruits'
tc.assertEqual(s[0:3], 'Eat')
tc.assertEqual(s[3:0], '') # if start>=stop with positive step, slice is empy
tc.assertEqual(s[:5], 'Eat m') 
tc.assertEqual(s[5:], 'ore fruits')
tc.assertEqual(s[:100], s) # all the way to the end
tc.assertEqual(s[4:8:2], 'mr')
tc.assertEqual(s[::3], 'E rfi')
tc.assertEqual(s[::-1], 'stiurf erom taE') # reverse order.

# goal: up to 18 positions around the found query
letters_amazon = '''
We spend several years building our own database engine,
Amazon Aurora, a fully managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as 
the commercial engines, but at one-tenth of the cost. We were
not supporised whe this worked.
'''

find = lambda s, q: s[s.find(q)-18: s.find(q)+18] if q in s else -1
print(find(letters_amazon, 'SQL'))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

sample = [line[::2] for line in price]
print(sample)

l = ['Firefox', 'corrupted', 'Chrome', 'corrupted']
g = ['Firefox', 'Firefox', 'Chrome', 'Chrome']

l[1::2] = l[::2]
tc.assertEqual(l,g)
print (l)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
tc.assertEqual([1,2,3]+[4,5], [1,2,3,4,5])
tc.assertEqual([1,2,3]+[4,5], [1,2,3,4,5])
tc.assertEqual([1,2,3]*3, [1,2,3,1,2,3,1,2,3])

import matplotlib.pyplot as plt

cardiac_cycle = [62,60,62,64,68,77,80,76,71,66,61,60,62]

expected_cycle = cardiac_cycle[1:-2] * 10

# plt.plot(expected_cycle)
# plt.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# general expressions: not stored in a list
s = sum([x**2 for x in range(20)])
general_expression = sum(x**2 for x in range(20))
tc.assertEqual(s, general_expression)

companies = {
    'CoolCompany': {'Alice':33, 'Bob': 28, 'Frank':29},
    'CheapCompany': {'Ann':4, 'Lee': 9, 'Chrisi':7},
    'SosoCompany': {'Esther':33, 'Cole': 8, 'Paris':29},
}

illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
print (companies['CoolCompany'].values())
print (illegal)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

l1 = [1,2,3]
l2 = [4,5,6]

zipped_list = list(zip(l1, l2))
tc.assertEqual(zipped_list, [(1,4), (2,5), (3,6)])

zipped_dict = dict(zip(l1, l2))
tc.assertEqual(zipped_dict, {1:4, 2:5, 3:6})

print (zipped_dict)

column_names = ['name','salary','job']
db_rows = [('Alice', 18000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

d = [dict(zip(column_names, x)) for x in db_rows]
print(d)