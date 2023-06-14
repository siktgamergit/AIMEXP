import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the file and extract the coordinates
filename = 'kalmar-fun.txt'
with open(filename, 'r') as f:
    lines = f.readlines()
x, y, z = [], [], []

lines = lines[0:5500]
for line in lines:
    coords = line.strip().split(',')
    x.append(float(coords[0]))
    y.append(float(coords[1]))
    z.append(float(coords[2]))
    #print(i)

# Define the acceleration vectors
u = np.zeros_like(x)
v = np.zeros_like(y)
w = np.zeros_like(z)
for i in range(len(x)-1):
    u[i] = x[i+1] - x[i]
    v[i] = y[i+1] - y[i]
    w[i] = z[i+1] - z[i]

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the line strip
ax.plot(x, y, z, linewidth=2, color='b')

# Add the acceleration vectors
for i in range(len(x)-1):
    ax.quiver(x[i], y[i], z[i], u[i], v[i], w[i], length=0.2, normalize=True)

# Set the labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()