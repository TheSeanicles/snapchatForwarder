import subprocess
import flask

class server:
    def init():
        pass

    def run():
        pass

    def test():
        pass

    def scratch():
        run1 = ['xdotool', 'search', '"Firefox ESR"', 'windowactivate', '--sync', 'key', '--clearmodifiers', 'ctrl+l']
        subprocess.run(run1)

if __name__ == '__main__':
    pass
