# https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium
import subprocess
import flask
import time
import os

class server:
    def init():
        pass

    def run():
        pass

    def test():
        pass

    def scratch():
        # run1 = ['xdotool', 'search', '"Mozilla Firefox"', 'windowactivate', '--sync', 'key', '--clearmodifiers', 'ctrl+l']
        # subprocess.run(run1)
        xdoCall = '/bin/bash -c "xdotool search "Mozilla Firefox" windowactivate --sync key --clearmodifiers ctrl+l"'
        os.system(xdoCall)

if __name__ == '__main__':
    pass
