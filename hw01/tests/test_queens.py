"""
八皇后求解器单元测试
测试目标：
1. N=4 时，合法方案数量必须为 2
2. N=8 时，合法方案数量必须为 92
"""

# 导入我们写的八皇后求解函数
from src.queens import solve_n_queens

def test_n_queens_4_solution_count():
    """测试 4 皇后问题的解数是否为 2"""
    # 调用求解函数，获取所有解
    solutions = solve_n_queens(4)
    # 断言解的数量等于 2
    assert len(solutions) == 2, "4 皇后问题的合法解数量应为 2"

def test_n_queens_8_solution_count():
    """测试 8 皇后问题的解数是否为 92"""
    # 调用求解函数，获取所有解
    solutions = solve_n_queens(8)
    # 断言解的数量等于 92
    assert len(solutions) == 92, "8 皇后问题的合法解数量应为 92"

# 可选：额外测试边界情况（比如 N=1），确保代码鲁棒性
def test_n_queens_1_solution_count():
    """测试 1 皇后问题的解数是否为 1"""
    solutions = solve_n_queens(1)
    assert len(solutions) == 1, "1 皇后问题的合法解数量应为 1"
