import forwardServer
import webbrowser
from multiprocessing import Process

if __name__ == '__main__':
    s = forwardServer.server
    s.run()
    s.scratch()
    webbrowser.get('Chromium').open_new_tab('google.com')