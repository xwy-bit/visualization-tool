import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider


def visualize_point_clouds_series(point_clouds):
    # Create figure and 3D axis
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Initialize point cloud scatter plot
    scatter = ax.scatter([], [], [])

    # Set axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Calculate the global range of all point clouds
    all_points = np.vstack(point_clouds)
    x_min, x_max = all_points[:, 0].min(), all_points[:, 0].max()
    y_min, y_max = all_points[:, 1].min(), all_points[:, 1].max()
    z_min, z_max = all_points[:, 2].min(), all_points[:, 2].max()

    # Set fixed axis ranges
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_zlim(z_min, z_max)

    # Create slider axis
    slider_ax = plt.axes([0.2, 0.02, 0.6, 0.03])
    slider = Slider(slider_ax, 'Frame', 0, len(point_clouds)-1, valinit=0, valstep=1)

    # Update function
    def update(val):
        frame = int(slider.val)
        points = point_clouds[frame]
        
        # Update scatter plot data
        scatter._offsets3d = (points[:, 0], points[:, 1], points[:, 2])
        
        # Update title
        ax.set_title(f'Point Cloud - Frame {frame}')
        
        fig.canvas.draw_idle()

    # Connect slider to update function
    slider.on_changed(update)

    # Initialize display
    update(0)

    plt.show()

if __name__ == '__main__':
    # Generate point cloud data
    num_frames = 100
    num_points = 100
    point_clouds = [np.random.randn(num_points, 3) for _ in range(num_frames)]

    # Visualize point clouds
    visualize_point_clouds(point_clouds)
