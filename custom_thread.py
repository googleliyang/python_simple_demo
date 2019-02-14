import threading


class CustomThread(threading.Thread):

    def __init__(self, lock):
        super().__init__()
        self.lock = lock
        self.i = 0

    def run(self):
        print('start run')
        for _ in range(10*1000000):
            self.i += 1
        print(self.i)


if __name__ == "__main__":
    lock = threading.Lock()
    t1 = CustomThread(lock)
    t2 = CustomThread(lock)
    t1.start()
    t2.start()
    # Default wait threading over main thread over but daemon
    print('--main thread run --')
