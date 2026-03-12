"""
八皇后问题求解器
功能：输入棋盘大小 N，输出所有合法的皇后摆放方案
原理：使用回溯算法，逐行放置皇后，同时检查列、对角线冲突
"""

def solve_n_queens(n: int) -> list[list[str]]:
    """
    求解 N 皇后问题，返回所有合法的摆放方案
    
    参数：
        n: 棋盘大小（皇后数量），整数类型
    
    返回：
        二维列表，每个子列表代表一个合法方案，子列表中的每个字符串代表棋盘的一行
    """
    # 存储所有合法解决方案
    solutions = []
    
    # board 数组：board[row] = col 表示第 row 行的皇后放在第 col 列
    # 初始值设为 -1，表示该行还未放置皇后
    board = [-1] * n

    def is_valid(row: int, col: int) -> bool:
        """
        检查在 (row, col) 位置放置皇后是否合法（无冲突）
        冲突类型：
        1. 列冲突：同一列已有皇后
        2. 对角线冲突：左上-右下 / 右上-左下对角线已有皇后
        """
        # 检查当前行之前的所有行（已放置皇后的行）
        for i in range(row):
            # 列冲突：第 i 行的皇后列号 = 当前尝试的列号
            if board[i] == col:
                return False
            # 对角线冲突：行差的绝对值 = 列差的绝对值
            if abs(row - i) == abs(col - board[i]):
                return False
        # 无冲突，合法
        return True

    def backtrack(row: int):
        """
        回溯算法核心：逐行放置皇后
        参数：row 表示当前要放置皇后的行号
        """
        # 终止条件：所有行都放置了皇后（找到一个合法方案）
        if row == n:
            # 将 board 数组转换为可视化的棋盘格式
            solution = []
            for i in range(n):
                # 初始化一行：全是 '.'
                line = ['.'] * n
                # 在皇后位置替换为 'Q'
                line[board[i]] = 'Q'
                # 拼接成字符串，加入当前方案
                solution.append(''.join(line))
            # 将当前方案加入总解决方案列表
            solutions.append(solution)
            return
        
        # 遍历当前行的所有列，尝试放置皇后
        for col in range(n):
            # 如果当前位置合法
            if is_valid(row, col):
                # 放置皇后：记录当前行的皇后列号
                board[row] = col
                # 递归处理下一行
                backtrack(row + 1)
                # 回溯：撤销当前行的皇后放置（恢复为 -1）
                board[row] = -1

    # 从第 0 行开始回溯
    backtrack(0)
    
    return solutions


# 测试代码（直接运行该文件时执行）
if __name__ == "__main__":
    # 示例1：求解 4 皇后问题
    n4_solutions = solve_n_queens(4)
    print(f"=== 4 皇后问题的所有解（共 {len(n4_solutions)} 个）===")
    for idx, solution in enumerate(n4_solutions, 1):
        print(f"方案 {idx}：")
        for line in solution:
            print(line)
        print()  # 空行分隔
    
    # 示例2：求解 8 皇后问题（只打印解的数量）
    n8_solutions = solve_n_queens(8)
    print(f"=== 8 皇后问题共有 {len(n8_solutions)} 个合法解 ===")
