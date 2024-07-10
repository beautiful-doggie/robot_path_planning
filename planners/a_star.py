import heapq

class AStarPlanner:
    def __init__(self, start, goal, obstacles):
        self.start = start
        self.goal = goal
        self.obstacles = obstacles

    def heuristic(self, node):
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def is_collision(self, node):
        for obs in self.obstacles:
            if obs[0] <= node[0] <= obs[2] and obs[1] <= node[1] <= obs[3]:
                return True
        return False

    def get_neighbors(self, node):
        neighbors = [
            (node[0] + 1, node[1]), (node[0] - 1, node[1]),
            (node[0], node[1] + 1), (node[0], node[1] - 1)
        ]
        return [neighbor for neighbor in neighbors if not self.is_collision(neighbor)]

    def plan(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {self.start: None}
        g_score = {self.start: 0}

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == self.goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(open_list, (f_score, neighbor))

        return []

if __name__ == "__main__":
    start = (0, 0)
    goal = (10, 10)
    obstacles = [(3, 3, 5, 5), (7, 8, 9, 9)]
    planner = AStarPlanner(start, goal, obstacles)
    path = planner.plan()
    print("规划路径:", path)
