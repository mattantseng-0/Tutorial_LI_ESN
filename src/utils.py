from matplotlib import pyplot as plt
import numpy as np

def lorenz_ts_plotter(x: np.ndarray, y: np.ndarray, z: np.ndarray, time: np.ndarray, num_points_to_plot: int = None, title_prefix: str = ""):
    if not num_points_to_plot:
        num_points_to_plot = len(time)

    plt.subplot(3, 1, 1)
    plt.plot(time[:num_points_to_plot], x[:num_points_to_plot], lw = 1)
    plt.title(title_prefix + "X")
    plt.xlabel("Time")
    plt.ylabel("X Amplitude")
    plt.grid(True)

    plt.subplot(3, 1, 2,)
    plt.plot(time[:num_points_to_plot], y[:num_points_to_plot], lw = 1)
    plt.title(title_prefix + "Y")
    plt.xlabel("Time")
    plt.ylabel("Y Amplitude")
    plt.grid(True)


    plt.subplot(3, 1, 3)
    plt.plot(time[:num_points_to_plot], z[:num_points_to_plot], lw = 1)
    plt.title(title_prefix + "Z")
    plt.xlabel("Time")
    plt.ylabel("Z Amplitude")
    plt.grid(True)

    plt.tight_layout()


def lorenz_3d_plotter(x: np.ndarray, y: np.ndarray, z: np.ndarray, num_points_to_plot: int = None, title_prefix = ""):
    if not num_points_to_plot:
        num_points_to_plot = len(x)

    ax = plt.figure().add_subplot(projection='3d')

    ax.plot(x[:num_points_to_plot], y[:num_points_to_plot], z[:num_points_to_plot], lw=.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title(title_prefix + "Lorenz Attractor")
    ax.set_box_aspect(None, zoom=0.85)
    
def lorenz_ts_train_target_compare(lorenz_training_data: np.ndarray,
                                   lorenz_target_data: np.ndarray,
                                   num_points_to_plot: int = None):
    if not num_points_to_plot:
        num_points_to_plot = len(lorenz_training_data[0, :])
    
    plt.subplot(3, 1, 1)
    plt.plot(lorenz_training_data[0, :num_points_to_plot])
    plt.plot(lorenz_target_data[0, :num_points_to_plot], "r--")
    plt.legend(["Training inputs", "Training targets"], loc='upper right')

    plt.title("Training X")
    plt.xlabel("Index")
    plt.ylabel("X Amplitude")

    plt.subplot(3, 1, 2,)
    plt.plot(lorenz_training_data[1, :num_points_to_plot])
    plt.plot(lorenz_target_data[1, :num_points_to_plot], "r--")
    plt.legend(["Training inputs", "Training targets"], loc='upper right')
    plt.title("Training Y")
    plt.xlabel("Index")
    plt.ylabel("Y Amplitude")


    plt.subplot(3, 1, 3)
    plt.plot(lorenz_training_data[2, :])
    plt.plot(lorenz_target_data[2, :], "r--")
    plt.legend(["Training inputs", "Training targets"], loc='upper right')


    plt.title("Training Z")
    plt.xlabel("Index")
    plt.ylabel("Z Amplitude")

    plt.tight_layout()
