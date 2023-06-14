import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap


def generate_animation(grid_list):
    # Convert the grid arrays to a numerical array
    grid_array = np.zeros((len(grid_list[0]), len(grid_list[0][0])), dtype=int)
    for i in range(len(grid_list[0])):
        for j in range(len(grid_list[0][0])):
            if grid_list[0][i][j] == -1:
                grid_array[i][j] = 3  # Yellow (Vaccinated)
            elif grid_list[0][i][j] == 0:
                grid_array[i][j] = 0  # Grey (Healthy)
            elif grid_list[0][i][j] == 1:
                grid_array[i][j] = 2  # Green (Immune)
            elif grid_list[0][i][j] > 1:
                grid_array[i][j] = 1  # Red (Ill)

    colors = ['grey', 'red', 'green', 'yellow']
    cmap = ListedColormap(colors)

    fig, ax = plt.subplots()
    img = ax.imshow(grid_array, cmap=cmap, interpolation='nearest', vmin=0, vmax=3)

    def update(frame):
        img.set_array(frame)
        return [img]

    anim = animation.FuncAnimation(fig, update, frames=grid_list, interval=500, blit=True)
    plt.show()
