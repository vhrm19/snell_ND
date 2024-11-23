import numpy as np
from generalized_snell import snell
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('Qt5Agg')

# Example vectors and parameters
incident = np.array([0.1, 0.1, 0.1])
normal = np.array([1, 0, 1])
v1 = 1.0
v2 = 1.0

# Compute refraction and reflection
T, R = snell(incident, normal, v1, v2)

# Plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors

origin = np.array([0, 0, 0])
xx, yy = np.meshgrid(range(-1, 2), range(-1, 2))
d = -origin.dot(normal)
z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

ax.plot_surface(xx, yy, z, alpha=0.1, rstride=10, cstride=10)
ax.quiver(*incident, *(-incident), color='blue', label='Incident')
ax.quiver(*origin, *normal, color='green', label='Normal', length=0.5)
ax.quiver(*origin, *T, color='orange', label='Refraction', length=0.5)
ax.quiver(*origin, *R, color='red', label='Reflection', length=0.5)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('3D Snell Law: Incident, Normal, Refraction, and Reflection Vectors')

plt.show()
