# функции и тип функции
a = 5
b = 11
def sum_num(arg1,arg2):
    return arg1 + arg2

x = sum_num(a,b)
y = sum_num(5,-x)
print(y)
print(type(sum_num))
print(type(type(sum_num)))

# стек функций(вызовов)

def g():
    print("I'm in function g")

def f():
    print("I'm in function f")
    g()
    print("I'm in function f")

print("I'm outside of any function")

f()

print("I'm outside of any function")