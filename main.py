import forwardServer
import subprocess
import time
from multiprocessing import Process

if __name__ == '__main__':
    s = forwardServer.server
    s.run()
    s.scratch()