import matplotlib.pyplot as plt
from planners.a_star import AStarPlanner
from planners.rrt import RRTPlanner
from controllers.pure_pursuit import PurePursuitController
from controllers.mpc import MPCController
from utils.environment import create_environment
from utils.visualization import plot_path, plot_tracking

def main():
    # 创建环境
    start, goal, obstacles = create_environment()

    # 路径规划
    a_star_planner = AStarPlanner(start, goal, obstacles)
    a_star_path = a_star_planner.plan()

    rrt_planner = RRTPlanner(start, goal, obstacles)
    rrt_path = rrt_planner.plan()

    # 绘制路径
    plot_path(a_star_path, obstacles, title="A* 路径规划")
    plot_path(rrt_path, obstacles, title="RRT 路径规划")

    # 路径跟踪
    pure_pursuit_controller = PurePursuitController()
    mpc_controller = MPCController()

    pure_pursuit_errors = pure_pursuit_controller.track(a_star_path)
    mpc_errors = mpc_controller.track(a_star_path)

    # 绘制跟踪误差
    plot_tracking(pure_pursuit_errors, title="纯跟踪误差")
    plot_tracking(mpc_errors, title="MPC 跟踪误差")

    # 显示结果
    plt.show()

if __name__ == "__main__":
    main()
