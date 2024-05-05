import numpy as np
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define the function for generating surface data
def f(x, y):
    """Generate surface data."""
    return np.sin(np.sqrt(x ** 2 + y ** 2))

# Function to get user input for generating data
def get_user_input():
    """Get user input for generating line and scattered points data."""
    # Getting user input for generating line data
    z_start = float(input("Enter the start value for z: "))
    z_end = float(input("Enter the end value for z: "))
    num_points = int(input("Enter the number of points for the line: "))
    z = np.linspace(z_start, z_end, num_points)
    x = np.sin(z)
    y = np.cos(z)

    # Plotting the line
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(x, y, z, 'grey')

    # Getting user input for generating scattered points data
    num_points = int(input("Enter the number of scattered points: "))
    z = 15 * np.random.random(num_points)
    x = np.sin(z) + 0.1 * np.random.randn(num_points)
    y = np.cos(z) + 0.1 * np.random.randn(num_points)

    # Plotting the scattered points
    ax.scatter3D(x, y, z, c=z, cmap='Greens')

    plt.show()

# Function to generate surface data
def generate_surface_data():
    """Get user input for generating surface data."""
    # Getting user input for generating surface data
    min_range = float(input("Enter the start value for x and y: "))
    max_range = float(input("Enter the end value for x and y: "))
    num_points = int(input("Enter the number of points for x and y: "))

    x = np.linspace(min_range, max_range, num_points)
    y = np.linspace(min_range, max_range, num_points)
    x, y = np.meshgrid(x, y)
    z = f(x, y)

    return x, y, z

# Function to plot surface data
def plot_surface(x, y, z):
    """Plot surface data."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Surface')
    plt.show()

# Function to plot contour of surface data
def plot_contour(x, y, z):
    """Plot contour of surface data."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.contour3D(x, y, z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Contour')
    plt.show()

# Function to plot wireframe of surface data
def plot_wireframe(x, y, z):
    """Plot wireframe of surface data."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, color='black')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Wireframe')
    plt.show()

if __name__ == "__main__":
    get_user_input()
    x, y, z = generate_surface_data()
    plot_surface(x, y, z)
    plot_contour(x, y, z)
    plot_wireframe(x, y, z)