import numpy as np
from scipy.optimize import minimize

class MPCController:
    def __init__(self, horizon=10, dt=0.1):
        self.horizon = horizon
        self.dt = dt

    def track(self, path):
        errors = []
        current_position = np.array(path[0], dtype=float)
        for i in range(1, len(path) - self.horizon):
            future_path = path[i:i + self.horizon]
            future_path = np.array(future_path, dtype=float).flatten()  # 将未来路径展平成一维数组
            current_position = np.tile(current_position, self.horizon)  # 将当前位置信息复制以匹配未来路径的长度
            res = minimize(self.objective, current_position, args=(future_path,), method='SLSQP', options={'maxiter': 50})
            current_position = res.x[:2]  # 更新当前位置为优化结果中的第一个点
            error = np.linalg.norm(current_position - future_path[:2])  # 计算当前位置与未来路径第一个点的误差
            errors.append(error)
        return errors

    def objective(self, u, future_path):
        u = np.reshape(u, (-1, 2))
        future_path = np.reshape(future_path, (-1, 2))
        total_error = 0
        for i in range(len(future_path)):
            total_error += np.linalg.norm(u[i] - future_path[i])
        return total_error

if __name__ == "__main__":
    path = [(0, 0), (2, 2), (4, 4), (6, 6), (8, 8), (10, 10)]
    controller = MPCController()
    errors = controller.track(path)
    print("跟踪误差:", errors)
