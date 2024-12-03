import forwardServer
import subprocess
import time
from multiprocessing import Process

if __name__ == '__main__':
    s = forwardServer.server
    s.run()
    def f():
        run1 = ['xdotool', 'search', '"Mozilla Firefox"', 'windowactivate', '--sync', 'key', '--clearmodifiers', 'ctrl+l']
        subprocess.call(run1)
    p = Process(target=f)
    p.start()
    time.sleep(5)
    p.join()