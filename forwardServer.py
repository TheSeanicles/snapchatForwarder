# https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium
import subprocess
import easyocr
from mss.linux import MSS as mss

class server:
    def init():
        # subprocess.call(['sh', './xdotoolScripts/openSnapchat.sh'])
        # Need to add this with multi-processing
        with mss(display=":0.0") as sct:
            for filename in sct.save():
                print(filename)
                reader = easyocr.Reader(['en'])
                result = reader.readtext(filename)
                print(result)


    def run():
        pass

    def test():
        pass

if __name__ == '__main__':
    pass
