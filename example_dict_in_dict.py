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
print(t[4][40])

print('----------------------------------------------------------------------------------------')
# Словарь из итерирующегося объекта.
my_dict_1 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

# Словарь из именованных аргументов.
my_dict_2 = dict(one=1, two=2, three=3)

# Словарь из списка кортежей.
my_dict_3 = dict([('two', 2), ('one', 1), ('three', 3)])

print(my_dict_1)
print(my_dict_2)
print(my_dict_3)