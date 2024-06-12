# thread_node.py

import threading
from operation import Operation

class ThreadNode:
    def __init__(self):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def run(self, context):
        for operation in self.operations:
            operation.execute(context)
