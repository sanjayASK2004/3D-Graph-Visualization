import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_user_input_points():
    num_points = int(input("Enter the number of points: "))
    x_points = np.zeros(num_points)
    y_points = np.zeros(num_points)
    z_points = np.zeros(num_points)
    for i in range(num_points):
        try:
            x_points[i] = float(input(f"Enter x-coordinate for point {i+1}: "))
            y_points[i] = float(input(f"Enter y-coordinate for point {i+1}: "))
            z_points[i] = float(input(f"Enter z-coordinate for point {i+1}: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return get_user_input_points()
    return x_points, y_points, z_points

def get_user_input_line():
    num_points = int(input("Enter the number of points for the line: "))
    x_line = np.zeros(num_points)
    y_line = np.zeros(num_points)
    z_line = np.zeros(num_points)
    for i in range(num_points):
        try:
            x_line[i] = float(input(f"Enter x-coordinate for point {i+1} of the line: "))
            y_line[i] = float(input(f"Enter y-coordinate for point {i+1} of the line: "))
            z_line[i] = float(input(f"Enter z-coordinate for point {i+1} of the line: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return get_user_input_line()
    return x_line, y_line, z_line

def get_user_input_surface():
    try:
        min_range = float(input("Enter the start value for x and y: "))
        max_range = float(input("Enter the end value for x and y: "))
        num_points = int(input("Enter the number of points for x and y: "))

        x_surface = np.linspace(min_range, max_range, num_points)
        y_surface = np.linspace(min_range, max_range, num_points)
        x_surface, y_surface = np.meshgrid(x_surface, y_surface)
        z_surface = np.sin(np.sqrt(x_surface**2 + y_surface**2))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return get_user_input_surface()

    return x_surface, y_surface, z_surface

# Getting user input for points
x_points, y_points, z_points = get_user_input_points()

# Plotting points
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_points, y_points, z_points, color='red', label='Points')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Points')
ax.legend()
plt.show()

# Getting user input for lines
x_line, y_line, z_line = get_user_input_line()

# Plotting lines
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_line, y_line, z_line, color='blue', label='Line')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Line')
ax.legend()
plt.show()

# Getting user input for surface
x_surface, y_surface, z_surface = get_user_input_surface()

# Plotting surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_surface, y_surface, z_surface, cmap='viridis', edgecolor='none')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface')
plt.show()

# Plotting contour of the surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.contour3D(x_surface, y_surface, z_surface, 50, cmap='binary')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Contour of the Surface')
plt.show()

# Plotting wireframe of the surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x_surface, y_surface, z_surface, color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wireframe of the Surface')
plt.show()
