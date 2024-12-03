# https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium
import subprocess
import flask
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
driver.close()

class server:
    def init():
        pass

    def run():
        pass

    def test():
        pass

if __name__ == '__main__':
    pass
