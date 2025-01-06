a = [12,6,34,21,9,25,16]
b = (25,12,9,36)
s = 0
for i in a:
  if i in b:
    s += i
  else:
    print(str(i))
print(str(s))