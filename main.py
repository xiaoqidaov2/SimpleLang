# main.py

from custom_parser import parse_structure

# 示例用户输入
user_input = """
开始
    - 线程
        - 赋值 x = MyInt(10)
        - 赋值 y = MyFloat(20.5)
        - 赋值 z = x + y
        - 赋值 c = MyComplex(1 + 2j)
        - 赋值 my_list = MyList(1, 2, 3)
        - 赋值 my_dict = MyDict(a=1, b=2)
        - 转换 y -> int
        - 转换 z -> float
        - 转换 c -> complex
        - 条件 x < y
            - 打印 "x 小于 y"
        - 逻辑 x == MyInt(10) and y == MyInt(20)
            - 打印 "x 是 10 且 y 是 20"
        - 打印 z
        - 打印 c
        - 打印 my_list
        - 打印 my_dict
"""


# 解析用户输入
lines = user_input.strip().split('\n')
start_node = parse_structure(lines)

# 运行程序
start_node.run()
