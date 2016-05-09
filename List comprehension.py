# Input Format

# Four integers X,Y,ZX,Y,Z and NN each on four separate lines, respectively.

# Output Format

# Print the list in lexicographic increasing order.

# Sample Input

# 1
# 1
# 1
# 2
# Sample Output

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x, y, z, n = (int(input()) for _ in range(4))
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])