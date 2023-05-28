import unittest
tc = unittest.TestCase()

name = '  ella fritzgerald  '

# string method
title = name.title()
tc.assertEqual(title, '  Ella Fritzgerald  ')

upper = name.upper()
print(upper)
lower = upper.lower()
print(lower)

lstrip = name.lstrip()
print(lstrip)
rstrip = name.rstrip()
print(rstrip)

stripped_name = name.strip()
print(stripped_name)

print(f"welcom back, {stripped_name}")
print(type(name))

three = '3'
type(three)
float_three = float(three)
print(float_three)

round = round(3.1415926, 2)
print(round)
print(abs(-5))
print(bin(20))
print(hex(20))

import math
print (math.sqrt(9))
print (math.pi)
print (math.log(100,10))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# list is a collection of items in a specific order. []
vowels = ['e', 'i', 'o']
print (vowels[0])
print (vowels[-1])
vowels.append('u') # add to the end
print (vowels)
vowels.insert(0, 'a') # insert at any position
print (vowels)

# modify 
vowels[-1] = 'y'
print (vowels)

airports = ['ANC', 'JNU', 'SEA', 'SIT']
tc.assertIn('SEA', airports)
airports.remove('SEA') # removes it directly from the list based on value
tc.assertNotIn('SEA', airports)

del airports[2]  # removes it directly from the list based om index
tc.assertNotIn('SIT', airports)

a = airports.pop() # pop last
b = airports.pop(0) # pop first
tc.assertListEqual([],airports)

# slicing
states = ['CA', 'CO', 'CT', 'DE', 'FL', 'GA']
sliced = states[2:4]
tc.assertTrue(all((x in states) for x in ['CT', 'DE']))
start = states[:2]
tc.assertTrue(all((x in start) for x in ['CA', 'CO']))
end = states[3:]
end2 = states[:-3]
tc.assertTrue(all((x in end)) for x in end2)

# copy of list without affecting the original list
my_state = states[:]
tc.assertTrue(all(x in my_state for x in states))
i = 'ASDF'
my_state.append(i)
tc.assertNotIn(i, states)
tc.assertIn(i, my_state)

# for loops let you work with each item in a list
for state in states:
    print (state)
    
# sort
vowels_original = ['a', 'i', 'e', 'u', 'o']
vowels = vowels_original[:]
sorted_ = sorted(vowels) # gives back a copy of sorted
for i in range(len(vowels_original)): #unchanged original list
    tc.assertEqual(vowels[i], vowels_original[i])
    # print (f'{vowels[i]} and {vowels_original[i]}')

vowels.sort() #changes original list
for i in range(len(vowels_original)):
    tc.assertEqual(vowels[i], sorted_[i])
    # print (f'{vowels[i]} and {sorted_[i]}')

# reverse sorting
vowels = vowels_original[:]
reverse = sorted(vowels, reverse=True)
vowels.sort(reverse=True)
for i in range(len(vowels_original)):
    tc.assertEqual(reverse[i], vowels[i])
    # print (f'{reverse[i]} and {vowels[i]}')

# to just reverse a list
vowels = vowels_original[:]
vowels.reverse()

# generate a series of numbers
nums = list(range(5))
print (nums)
tc.assertEqual(nums, [0,1,2,3,4])
nums = list (range(95, 100))
tc.assertEqual(nums, [95, 96, 97, 98, 99])
odd = list (range(1, 10, 2))
tc.assertEqual(odd, [1,3,5,7,9])

# pattern for powers of 10
nums = []
for e in range(5):
    nums.append(10**e)
print (nums)
tc.assertEqual(nums, [1,10,100,1000,10000])

#list comprehension: compact way of defining a list
nums = [10**e for e in range(5)]
tc.assertEqual(nums, [1,10,100,1000,10000])

states = ['CA', 'CO', 'CT']
lower = [s.lower() for s in states] # list comprohension I am able te change any item in the list
tc.assertEqual(lower, ['ca', 'co', 'ct'])

# tuple: ordered collection of items that cannot be modified
grades = (2, 3, 4)
for g in grades:
    print (f'you have a {g}!')
# grades[0] = 1 results in error 'tuple' object does not support item assignment

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Dictionaries: a set of items; each item consist of key and value
capital = { # Create
    'AK' : 'Junea',
    'AL' : 'Montgomery',
    'AZ' : 'Phoenix'
}
tc.assertEqual(capital['AK'], 'Junea') # Read
# capital['asdf'] gives KeyError: 'asdf'
capital['AR'] = 'Little Rock' # Modify
print(capital) 
tc.assertDictEqual({'AR' : 'Little Rock', 'AK' : 'Junea', 'AL' : 'Montgomery', 'AZ' : 'Phoenix'}, capital)
del capital['AR'] # Delete
tc.assertDictEqual({'AK' : 'Junea', 'AL' : 'Montgomery', 'AZ' : 'Phoenix'}, capital)

json = {'id': '123234-34234-23234-234', 'event': {'time': '20120312-12:00:02', 'state':'on'}}
tc.assertEqual(json.get('id'), '123234-34234-23234-234')
tc.assertEqual(json.get('event').get('state'), 'on')
tc.assertEqual(json.get('blablabla'), None) # will get a None if key doesnt exist
default = 'I do not exist'
tc.assertEqual(json.get('blablabla', default), default) # possible to give a default respond

# get all the keys values or items, helpers for iterating through them
print(f'keys {json.keys()}') 
print(f'values {json.values()}') 
print(f'items {json.items()}') 

j = []
for s in json:
    j.append(s)
tc.assertEqual(['id', 'event'], j)

j = []
for s in json.values():
    j.append(s)
tc.assertEqual(['123234-34234-23234-234', {'time': '20120312-12:00:02', 'state':'on'}], j)

j = []
l = []
for key, value in json.items(): # items give back both key and value
    j.append(key)
    l.append(value)
tc.assertEqual(['id', 'event'], j)
tc.assertEqual(['123234-34234-23234-234', {'time': '20120312-12:00:02', 'state':'on'}], l)

# list in dictionaries
states_visited = {'Eric': ['AK','WY','WA','NH'], 'Isaac': ['CO','NY','AK']}
for name, states in states_visited.items():
    print(f'{name} has visited:')
    for state in states:
        print(f' {state}')
        
# dictionaries in list
musicians = [{'first': 'Ella'}, {'first': 'Janis'}]
t = []
for m in musicians:
    print(f"test {m.get('first')} ")  
    t.append(m.get('first'))
tc.assertTrue(all(x in ['Ella', 'Janis'] for x in t)) 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# check if item is in a list
l = ['a', 'b', 'c', 'd']
if 'g' in l:
    tc.assertFalse(True)
    
plant_height = 10
a = 0
if plant_height < 3:
    a = 1
    print('keep it in the greenhouse!')
elif plant_height < 15:
    a = 2
    print('Move outside')
else:
    a = 3
    print('request to harvast')
    
tc.assertEqual(a, 2)

num = 0
while num < 3:
    print (num)
    num += 1

tc.assertEqual(num,3)

l = ['a', 'b', 'c', 'd']

# a while loops as long as condition is True:
while l:
    print(l)
    l.pop(-1)
    
l = list(range(0,100))
number = 0
while True:
    number = l.pop(0)
    if number == 50:
        break
    elif number != 50:
        continue
    else:
        print('should not occur')
        tc.assertTrue(False)
        
tc.assertEqual(number, 50)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def hello(t):
    t += 1
    tc.assertEqual(t, 1)
    print('hello')
    
t = 0
hello(t)
tc.assertEqual(t, 0) # value of t did not change!

# arbitrarary positional arguments
def post_message(user, *msgs):
    print(f"{user} saids:")
    for msg in msgs:
        print(f'{msg}')
    
post_message('harry', 'asd','fgh','hjk')

# keyword arguments:
def desc_user(user, **desc):
    print(f"{user} descibed as:")
    for key, value in desc.items():
        print(f' {key} is {value}')
    
desc_user('harry', active=True, email="asdf@gmail.com", num=234)

# defaults values in parameters
def coffee(size = 12):
    print(f'my coffee size is {size}')
    return size

tc.assertEqual(12, coffee())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Trail():
    def __init__(self, dest, len=0): #self references the current instance of the class.
        self.dest = dest
        self.len = len
    
    def describe(self):
        desc = f'This trail goes to {self.dest}'
        if self.len:
            desc += f'\nThe trail is {self.len} km.'
        return desc
    
    def runt(self):
        print(f'Running to {self.dest} by foot.')

t = Trail('Jamaica', 100)
tc.assertEqual('This trail goes to Jamaica\nThe trail is 100 km.', t.describe())

class BikeTrail(Trail):
    def __init__(self, dest, len=0, bikes_only = True):
        super().__init__(dest, len)
        self.paved = True
        self.bikes_only = bikes_only
    
    def ride(self):
        print(f'Riding to {self.dest} by bike.')
    
    def runt(self):
        if self.bikes_only:
            print('You cannot run this trail')
        else:
            super().runt()

bt = BikeTrail('China', 10000, False)
desc = bt.describe()
print(f'{desc}')
bt.ride()
bt.runt()

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

filename = 'test_cards.py' # this code

f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())
    
print(lines)
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
