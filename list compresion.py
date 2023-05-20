x, y, z, n = [int(input()) for _ in range(4)]
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(coordinates)
# gives combination of  the 3 D coordinates in the system
