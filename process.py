# multiple process 
# common resource

import multiprocessing 
import time
import os


def run_process(tag, queue):
    print('tag is %s' %tag)
    child_process = multiprocessing.current_process()
    print('process id %s' %child_process.pid)
    print('process id %s' %os.getpid())
    print('child parent process pid is %s' %os.getppid())
    for i in range(1, 5):
        queue.put(i)


def read_queue(queue):
    while not queue.empty():
        # Mac not support this method  queue.qsize()
        print('Get one of queue value is %s' % queue.get())
    print('Right now, the queue is empty!')


def test():
    queue = multiprocessing.Queue(5)
    # create subprocess
    p1 = multiprocessing.Process(target=run_process, args=(1, queue))
    p2 = multiprocessing.Process(target=read_queue, args=(queue, ))
    p1.start()
    p1.join()
    p2.start()
    # destroy child process
    # p1.terminate()


if __name__ == "__main__":
    current_process = multiprocessing.current_process()
    print('main process run id is %s' %current_process.pid)
    test()
