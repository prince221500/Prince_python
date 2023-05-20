n = int(input("enter the number of rows"))
for i in range(65, n + 65):
  for j in range(65, i + 1):
    print(chr(j), end=" ")
  print()