n = [2, 8, 9, 48, 8, 22, -12, 2]
m=[]
for number in n:
    if number >5:
      m.append(number + 2)
      w = list(set(m))
print(n)
print(w)