a = [1,2,1]
temp = 0
b = []
for x in a:
  b.append(temp + x)
  temp = x
  #print(b)
b.append(1)
print(b)

for i in range(100):
  a = b
  temp = 0
  b = []
  for x in a:
    b.append(temp + x)
    temp = x
    #print(b)
  b.append(1)
  print(b)