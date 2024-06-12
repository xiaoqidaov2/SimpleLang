# custom_parser.py

from start_node import StartNode
from thread_node import ThreadNode
from operation import Operation

def parse_line(line):
    indent_level = len(line) - len(line.lstrip())
    content = line.strip().lstrip('-').strip()
    return indent_level, content

def parse_structure(lines):
    start_node = StartNode()
    current_threads = []
    current_operations = []
    current_indent = -1

    for line in lines:
        line = line.strip()
        if line.startswith("#") or not line:
            continue  # 跳过注释和空行

        indent_level, content = parse_line(line)

        if content.startswith("线程"):
            thread = ThreadNode()
            start_node.add_thread(thread)
            current_threads.append((indent_level, thread))
            current_operations = []
        else:
            if content.startswith("打印"):
                operation = Operation("打印", content.split(" ", 1)[1])
            elif content.startswith("赋值"):
                operation = Operation("赋值", content.split(" ", 1)[1])
            elif content.startswith("条件"):
                operation = Operation("条件", content.split(" ", 1)[1])
            elif content.startswith("逻辑"):
                operation = Operation("逻辑", content.split(" ", 1)[1])
            elif content.startswith("转换"):
                operation = Operation("转换", content.split(" ", 1)[1])
            else:
                continue  # 未知操作，跳过

            if current_operations:
                last_indent, last_op = current_operations[-1]
                if indent_level > last_indent:
                    last_op.add_sub_operation(operation)
                else:
                    while current_operations and current_operations[-1][0] >= indent_level:
                        current_operations.pop()
                    if current_operations:
                        current_operations[-1][1].add_sub_operation(operation)
                    else:
                        current_threads[-1][1].add_operation(operation)
            else:
                current_threads[-1][1].add_operation(operation)
            current_operations.append((indent_level, operation))

    return start_node
