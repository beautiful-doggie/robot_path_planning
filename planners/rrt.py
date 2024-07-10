import random
import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

class RRTPlanner:
    def __init__(self, start, goal, obstacles, max_iter=500, step_size=1.0):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.obstacles = obstacles
        self.max_iter = max_iter
        self.step_size = step_size
        self.nodes = [self.start]

    def distance(self, node1, node2):
        return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

    def is_collision(self, node):
        for obs in self.obstacles:
            if obs[0] <= node.x <= obs[2] and obs[1] <= node.y <= obs[3]:
                return True
        return False

    def get_random_node(self):
        rand_x = random.uniform(0, 10)
        rand_y = random.uniform(0, 10)
        return Node(rand_x, rand_y)

    def get_nearest_node(self, random_node):
        nearest_node = self.nodes[0]
        min_dist = self.distance(random_node, nearest_node)
        for node in self.nodes:
            dist = self.distance(random_node, node)
            if dist < min_dist:
                nearest_node = node
                min_dist = dist
        return nearest_node

    def plan(self):
        for _ in range(self.max_iter):
            rand_node = self.get_random_node()
            nearest_node = self.get_nearest_node(rand_node)
            theta = math.atan2(rand_node.y - nearest_node.y, rand_node.x - nearest_node.x)
            new_node = Node(nearest_node.x + self.step_size * math.cos(theta), nearest_node.y + self.step_size * math.sin(theta))
            if not self.is_collision(new_node):
                new_node.parent = nearest_node
                self.nodes.append(new_node)
                if self.distance(new_node, self.goal) < self.step_size:
                    self.goal.parent = new_node
                    self.nodes.append(self.goal)
                    return self.get_final_path()
        return []

    def get_final_path(self):
        path = []
        node = self.goal
        while node:
            path.append((node.x, node.y))
            node = node.parent
        return path[::-1]

if __name__ == "__main__":
    start = (0, 0)
    goal = (10, 10)
    obstacles = [(3, 3, 5, 5), (7, 8, 9, 9)]
    planner = RRTPlanner(start, goal, obstacles)
    path = planner.plan()
    print("规划路径:", path)
