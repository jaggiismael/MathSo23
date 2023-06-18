import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def generate_animation(grid_list, save_path='animation.mp4'):
    # Check for NaN and infinity values in grid_list and replace them with 0
    grid_list = [np.where(np.isnan(grid) | np.isinf(grid), 0, grid) for grid in grid_list]

    # Define custom colormap
    cmap = colors.ListedColormap(['Yellow', 'Grey', 'Green', 'Red'])

    # Define the color boundaries
    bounds = [-1.5, -0.5, 0.5, 1.5, 1e10]  # Replace np.inf with a large number
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    # Initialize the image with the first grid_array
    img = ax.imshow(grid_list[0], cmap=cmap, norm=norm)
    plt.colorbar(img, ticks=[-1, 0, 1, 2], ax=ax, extend='both')  # Update the colorbar function
    plt.title("Grid Array Visualization")

    # Update function for the animation
    def update(frame):
        img.set_array(frame)
        return [img]

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=grid_list, interval=500, blit=True)

    # Save the animation
    writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    anim.save(save_path, writer=writer)


    # Show the animation
    plt.show()


def generate_3d_animation(grid_list):
    # Check for NaN and infinity values in grid_list and replace them with 0
    grid_list = [np.where(np.isnan(grid) | np.isinf(grid), 0, grid) for grid in grid_list]

    # Define custom colormap
    cmap = colors.ListedColormap(['Yellow', 'Grey', 'Green', 'Red'])

    # Define the color boundaries
    bounds = [-1.5, -0.5, 0.5, 1.5, 1e10]  # Replace np.inf with a large number
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create the figure
    fig = plt.figure(figsize=(8, 6))

    # Create the 3D axis
    ax = fig.add_subplot(111, projection='3d')

    # Get the X, Y coordinates for the grid
    X, Y = np.meshgrid(np.arange(grid_list[0].shape[1]), np.arange(grid_list[0].shape[0]))

    # Initialize the surface plot with the first grid_array
    Z = grid_list[0]
    colors_array = cmap(norm(Z.flatten())).reshape(Z.shape + (4,))
    surf = ax.plot_surface(X, Y, Z, facecolors=colors_array, rstride=1, cstride=1)

    plt.title("Grid Array Visualization (3D)")

    # Update function for the animation
    def update(frame):
        ax.clear()
        Z = frame
        colors_array = cmap(norm(Z.flatten())).reshape(Z.shape + (4,))
        surf = ax.plot_surface(X, Y, Z, facecolors=colors_array, rstride=1, cstride=1)
        return [surf]

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=grid_list, interval=500, blit=False)

    # Show the animation
    plt.show()


def plot_recurrence(grid_list):
    # Count the recurrence of each number in each grid
    recurrence_counts = []
    for grid in grid_list:
        unique, counts = np.unique(grid, return_counts=True)
        recurrence_counts.append(dict(zip(unique, counts)))

    # Create a line chart
    fig, ax = plt.subplots(figsize=(8, 6))

    # Define the number-label mapping
    number_label_mapping = {-1: "Vaccinated", 0: "Not concerned", 1: "Healthy"}

    for number, label in number_label_mapping.items():
        count_list = [recurrence[number] if number in recurrence else 0 for recurrence in recurrence_counts]
        ax.plot(count_list, label=label)

    # Handle the case for numbers less than 1
    count_list = [sum(recurrence[number] for number in recurrence if number > 1) for recurrence in recurrence_counts]
    ax.plot(count_list, label="Ill")

    ax.set_xlabel('Days')
    ax.set_ylabel('Number of people')
    ax.set_title('Population State')
    ax.legend()

    plt.show()