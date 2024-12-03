# https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium
import subprocess
import keras_ocr
from mss.linux import MSS as mss

class server:
    def init():
        # subprocess.call(['sh', './xdotoolScripts/openSnapchat.sh'])
        # Need to add this with multi-processing
        with mss(display=":0.0") as sct:
            for filename in sct.save():
                print(filename)
                pipeline = keras_ocr.pipeline.Pipeline()
                images = [
                            keras_ocr.tools.read(img) for img in [filename]
                        ]
                # generate text predictions from the images
                prediction_groups = pipeline.recognize(images)
                predicted_image = prediction_groups[1]
                for text, box in predicted_image:
                    print(text)


    def run():
        pass

    def test():
        pass

if __name__ == '__main__':
    pass
