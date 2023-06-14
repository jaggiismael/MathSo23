import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# Define the colors for different bed states
colors = ['grey', 'green', 'red', 'yellow']
cmap = ListedColormap(colors)

def generate_animation(grid_list):
    # Convert the grid arrays to a numerical array
    grid_array = np.zeros((len(grid_list[0]), len(grid_list[0][0])), dtype=int)
    for i in range(len(grid_list[0])):
        for j in range(len(grid_list[0][0])):
            if grid_list[0][i][j] == 'healthy':
                grid_array[i][j] = 0
            elif grid_list[0][i][j] == 'ill':
                grid_array[i][j] = 1
            elif grid_list[0][i][j] == 'immune':
                grid_array[i][j] = 2
            elif grid_list[0][i][j] == 'vaccinated':
                grid_array[i][j] = 3

    fig, ax = plt.subplots()
    img = ax.imshow(grid_array, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)

    def update(frame):
        img.set_array(frame)
        return [img]

    anim = animation.FuncAnimation(fig, update, frames=grid_list, interval=500, blit=True)
    plt.show()
