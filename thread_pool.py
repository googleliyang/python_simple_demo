# init process poll
# use pool deal process
# if poll is full, waitting for pool release

import multiprocessing
import time


def run():
    time.sleep(3)
    print('multiprocess is run')


if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    # * the last print will print after 6s, because the pool only accommodate three thread
    for _ in range (4):
        # by async method the main thread process not wait, apply main thread wait ? why , read  your note !
        pool.apply_async(run)
    # close pool after close pool will never accept new task
    pool.close()
    # *must call after close or terminate
    # If main thread dead, the child process will dead, such like kill parent id in terminal
    pool.join()
