n = int(input("enter the number of rows"))
y = n - 1
sp = " "
x = 1
while (x < n):
  print(sp * y + "*" * x)
  x = x + 1
  y = y - 1
