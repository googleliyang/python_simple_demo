import threading
# custom thread
total = 1
def thread_(lock):
    global total
    for _ in range(100*10000):
        with lock:
            total += 1
    print('The total is %s' % total)

def test(): 
   lock = threading.Lock()
   t1 = threading.Thread(target=thread_, args=(lock,))
   t2 = threading.Thread(target=thread_, args=(lock,))
   t1.start()
   t2.start()

if __name__ == "__main__":
    test()
       