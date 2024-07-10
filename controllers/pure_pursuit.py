import numpy as np

class PurePursuitController:
    def __init__(self, lookahead_distance=1.0):
        self.lookahead_distance = lookahead_distance

    def track(self, path):
        errors = []
        current_position = np.array(path[0], dtype=float)
        for waypoint in path[1:]:
            waypoint = np.array(waypoint, dtype=float)
            error = np.linalg.norm(current_position - waypoint)
            errors.append(error)
            direction = (waypoint - current_position) / error
            current_position += direction * self.lookahead_distance
        return errors

if __name__ == "__main__":
    path = [(0, 0), (2, 2), (4, 4), (6, 6), (8, 8), (10, 10)]
    controller = PurePursuitController()
    errors = controller.track(path)
    print("跟踪误差:", errors)
