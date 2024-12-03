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
        run1 = 'xdotool search "Mozilla Firefox" windowactivate --sync key --clearmodifiers ctrl+l'
        run1 = 'neofetch'
        subprocess.run(run1, check=True, stdout=subprocess.PIPE, executable="/bin/bash")
        print(run1.stdout)

if __name__ == '__main__':
    pass
