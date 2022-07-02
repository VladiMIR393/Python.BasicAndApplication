objects = [True, False, True, 3, True, 1, 2, 3, 4, 1, 2, 3, 3, 'True', 'False', 'g']
#objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2], [1,2], [1,2]]
ans = 0
m = []
# неверное, хоть и засчитанное решение

for obj in objects: # доступная переменная objects
    if obj not in m:
        m.append(obj)
        ans += 1
# верное и забавное решение

p = set()
for obj in objects:
    p.add(id(obj))

print(ans)
print(len(p))

