# data structures numpy
# Reqwests to yahoo and update view

import requests
import threading
import queue
import time

class Model:
    def __init__(self):
        pass
    def link(self, controller):
        self.controller = controller
        pass

    def load(self):
        self.message_queue = queue.Queue()
        self.lock = threading.Lock()
        self.lock.acquire()
        self.model_thread = threading.Thread(name="model", target=modelMain , args=(self.message_queue,self.lock) )
        self.model_thread.start()

    def communicate(self, callback):
        self.message_queue.put(callback)
        self.lock.release()

def modelMain(message_queue , lock):
    print("Model thread waiting")
    while True:
        lock.acquire()
        print("Model thread unlocked")
        message = message_queue.get()
        if callable(message):
            message()
        else:
            print(message)