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
        run1 = 'xdotool type "neofetch"; xdotool key KP_Enter'
        run1 = ('xdotool', 'type "neofetch"')
        run2 = ('xdotool', 'key KP_Enter')
        subprocess.run(run1)
        
        subprocess.run(run2, check=True, stdout=subprocess.PIPE).stdout
        print(run2.stdout)

if __name__ == '__main__':
    pass
