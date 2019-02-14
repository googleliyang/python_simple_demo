# Thread lock
# File open

'''
    # For thread operation
    # threading.Lock() self.lock.acquire() lock.release()
    # class lock __enter__ return lock.acquire() exit() lock.release
    with lock:
        pass
        a += 1
    # For file operation
    with open('test', 'w') as f:
        f.write('Python大法好')
'''

class CustomOpen:

    def __init__(self, file, mode):
        self.__file = file
        self.__mode = mode

    def __enter__(self):
        self.__handle = open(self.__file, self.__mode)
        print('Exec enter')
        return self.__handle

    def __exit__(self, exc_type, exc_var, exc_tb):
        if exc_type:
            print('Get a exception!') 
        print('Exec exit')
        self.__handle.close()
        # If return true with will catch the except
        return True

def test():
    # with CustomOpen('a.txt', 'w') as item:
     with CustomOpen('a.txt', 'r') as item:
        item.write('New year new begin')

if __name__ == "__main__":
    test()

    