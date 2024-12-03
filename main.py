import forwardServer
import subprocess
import time
from multiprocessing import Process

if __name__ == '__main__':
    s = forwardServer.server
    s.run()
    def f():
        subprocess.call(['sh', './script.sh'])
    p = Process(target=f)
    p.start()
    time.sleep(5)
    p.join()