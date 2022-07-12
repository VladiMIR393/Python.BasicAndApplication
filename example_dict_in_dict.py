import collections

t = {1: 1}
print(t)
t.update({2: {21: 22}, 3: {31: 33}})
print(t)
t.update([[4,{40: 41}],[5, {54: 55}]])
print(t)
t.setdefault(6)
print(t)
t.setdefault(7, {71: 72})
print(t)
# {1: 1}
# {1: 1, 2: {21: 22}, 3: {31: 33}}
# {1: 1, 2: {21: 22}, 3: {31: 33}, 4: {40: 41}, 5: {54: 55}}
# {1: 1, 2: {21: 22}, 3: {31: 33}, 4: {40: 41}, 5: {54: 55}, 6: None}
# {1: 1, 2: {21: 22}, 3: {31: 33}, 4: {40: 41}, 5: {54: 55}, 6: None, 7: {71: 72}}
print('----------------------------------------------------------------------------------------')
w = {"1": {"11": 11}, "2": {"22": 22}}
scopes = {'global': {'parent': None, 'variables': []}}
print(scopes)
scopes['global']['variables'] = ['a']
#create foo global

scopes.update([['foo',{'parent': 'global', 'variables': []}]])
print(scopes)
scopes['foo']['variables'] += ['b']
print(scopes)
scopes['foo']['variables'] += ['c']
print(scopes)
print('a' in scopes['foo']['variables'])

print('----------------------------------------------------------------------------------------')