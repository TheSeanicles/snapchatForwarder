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
        subprocess.run(run1, check=True, stdout=subprocess.PIPE, executable="/bin/bash").stdout
        print(run1.stdout)

if __name__ == '__main__':
    pass
