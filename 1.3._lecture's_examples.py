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

# стек как список

x = [1,2,3]
x.append(4)
x.append(5)
print(x)

top = x.pop()
print(top)
print(x)

top = x.pop()
print(top)
print(x)

# None пример

x = print(10)
print(x)
print(type(x))
print(x is not None)

def s(a, *vs, b=10):
   print(a)
   print(b)
   res = a + b
   print(res)
   for v in vs:
       print(v)
       res += v
   print(res)
   return res

s(5,5,5,5,1)
