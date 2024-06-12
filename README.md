## SimpleLang 项目文档

### 声明

我是人工智能模型 ChatGPT4o，本项目的代码和文档由我生成。希望这能为您提供帮助和参考。如有任何问题或反馈，请随时联系我。

### 项目概述

SimpleLang 是一个简单的编程语言示例，展示了如何使用自定义类型和操作。该项目包含以下主要功能：

- 自定义类型：包括整数、浮点数、复数、列表和字典。
- 基本操作：赋值、打印、条件判断、逻辑判断和类型转换。
- 多线程支持：可以定义多个线程并行执行操作。
- 简单的解析器：解析用户输入的结构化文本并执行相应的操作。

### 目录结构

```
SimpleLang/
│
├── custom_types.py
├── operation.py
├── thread_node.py
├── start_node.py
├── parser.py
└── main.py
```

### 文件说明

- **custom_types.py**：定义了自定义类型 `MyInt`、`MyFloat`、`MyComplex`、`MyList` 和 `MyDict` 及其基本操作。
- **operation.py**：定义了 `Operation` 类，包含各种操作的执行逻辑。
- **thread_node.py**：定义了 `ThreadNode` 类，用于在多线程环境中执行操作。
- **start_node.py**：定义了 `StartNode` 类，负责启动并管理多个线程。
- **parser.py**：包含解析器逻辑，将用户输入的结构化文本解析为操作结构。
- **main.py**：项目的入口，包含示例用户输入并执行解析和运行操作。

### 安装说明

1. **创建项目目录**：创建一个名为 `SimpleLang` 的目录，并在其中创建上述文件。
2. **编写代码**：将上述代码分别复制到相应的文件中。

### 使用说明

1. **编辑用户输入**：在 `main.py` 中编辑用户输入，定义要执行的操作。例如：

    ```python
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
    ```

2. **运行程序**：在终端中导航到 `SimpleLang` 目录，运行 `python main.py`。

    ```sh
    $ cd SimpleLang
    $ python main.py
    ```

### 示例输出

运行上述示例用户输入，程序将输出以下内容：

```
x 是 10 且 y 是 20
30.5
(1+2j)
[1, 2, 3]
{'a': 1, 'b': 2}
```

### 注意事项

- 该项目仅为示例项目，展示了如何实现一个简单的编程语言解析和执行引擎。
- 代码中包含的功能和操作较为基础，实际使用中可以根据需求进行扩展和优化。

### 贡献指南

欢迎对本项目进行贡献！如有任何建议或改进，请提交 Issue 或 Pull Request。

### 开源许可

本项目遵循 MIT 许可证。详细信息请参见 LICENSE 文件。

---

感谢使用 SimpleLang 项目！希望它能对您的学习和开发有所帮助。
