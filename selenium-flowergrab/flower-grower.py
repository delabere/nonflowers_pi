"""
This file is just a test to make sure that we can run
selenium fine on the pi
If we can then we can move onto bigger things
"""

print("importing libraries...")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# run headless
print("setting options...")
chrome_options = Options()

chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")

# make sure to install the driver first and put
# it in the same directory
print("initialising driver...")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome("./chromedriver", options=chrome_options)

# load a webpage
print("loading webpage...")
# driver.get("https://www.python.org")
driver.get("http://nonflowers.lingdong.works/")

print("waiting to make sure page has loaded...")
time.sleep(20)
print("executing script...")
driver.execute_script("makeDownload()")
print("waiting to make sure file has downloaded...")
time.sleep(10)
# should be "Welcome to Python.org"
title = driver.title

# close
driver.close()

print(title)