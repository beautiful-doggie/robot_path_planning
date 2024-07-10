import matplotlib.pyplot as plt

def plot_path(path, obstacles, title="路径规划"):
    fig, ax = plt.subplots()
    for obs in obstacles:
        rect = plt.Rectangle((obs[0], obs[1]), obs[2] - obs[0], obs[3] - obs[1], color='red')
        ax.add_patch(rect)
    path_x, path_y = zip(*path)
    ax.plot(path_x, path_y, marker='o')
    ax.plot(path_x[0], path_y[0], marker='s', color='green')  # 起点
    ax.plot(path_x[-1], path_y[-1], marker='x', color='blue')  # 终点
    ax.set_title(title)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    plt.grid(True)

def plot_tracking(errors, title="跟踪误差"):
    plt.figure()
    plt.plot(errors)
    plt.title(title)
    plt.xlabel('时间步')
    plt.ylabel('跟踪误差 (米)')
    plt.grid(True)
