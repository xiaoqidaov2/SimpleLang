# start_node.py

import threading
from thread_node import ThreadNode

class StartNode:
    def __init__(self):
        self.threads = []

    def add_thread(self, thread_node):
        self.threads.append(thread_node)

    def run(self):
        threads = []
        context = {}
        for thread_node in self.threads:
            t = threading.Thread(target=thread_node.run, args=(context,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
