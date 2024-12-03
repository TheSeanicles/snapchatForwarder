import time
import forwardServer

if __name__ == '__main__':
    s = forwardServer.server
    s.run()
    s.scratch()
    time.sleep(5)
    # input("Press return to close the program")