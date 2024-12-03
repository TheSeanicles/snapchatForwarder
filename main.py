import time
import forwardServer

if __name__ == '__main__':
    time.sleep(5)
    s = forwardServer.server
    s.run()
    s.scratch()