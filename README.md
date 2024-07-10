# 移动机器人路径规划和跟踪

本项目模拟移动机器人在二维环境中的路径规划和跟踪过程。

## 项目结构

- `main.py`: 仿真主入口。
- `planners/`: 包含不同的路径规划算法。
- `controllers/`: 包含不同的路径跟踪控制器。
- `utils/`: 环境设置和可视化的工具函数。
- `data/`: 存储结果和日志。

## 设置

1. 克隆代码库：
    ```sh
    git clone https://github.com/yourusername/robot_path_planning.git
    cd robot_path_planning
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

## 使用

运行主仿真脚本：
```sh
python main.py
