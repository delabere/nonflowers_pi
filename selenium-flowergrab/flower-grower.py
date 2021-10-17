"""
This file is just a test to make sure that we can run
selenium fine on the pi
If we can then we can move onto bigger things
"""

print("importing libraries...")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

start = time.time()

# run headless
print("setting options...")
chrome_options = Options()

chrome_download_dir = r'C:\Users\jackr\Desktop\projects\nonflowers_pi\selenium-flowergrab\\'
chrome_download_dir = os.getcwd()

chrome_options.add_argument("--headless")
prefs = {'download.default_directory' : chrome_download_dir}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument("--no-sandbox")
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
# time.sleep(20)
driver.save_screenshot("screenshot.png")
print("executing script...")
driver.execute_script("makeDownload()")
print("waiting to make sure file has downloaded...")
time.sleep(5)
# should be "Welcome to Python.org"
title = driver.title

# close
driver.close()

end = time.time()
print(f"time taken: {end-start} seconds...")
