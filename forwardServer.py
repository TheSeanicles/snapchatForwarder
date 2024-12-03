# https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium
import subprocess
import flask
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()

class server:
    def init():
        pass

    def run():
        pass

    def test():
        pass

    def scratch():
        run1 = ['xdotool', 'search', '"Mozilla Firefox"', 'windowactivate', '--sync', 'key', '--clearmodifiers', 'ctrl+l']
        subprocess.run(run1)

if __name__ == '__main__':
    pass
