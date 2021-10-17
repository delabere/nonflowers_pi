"""
This file is just a test to make sure that we can run
selenium fine on the pi
If we can then we can move onto bigger things
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# run headless
print("setting options...")
chrome_options = Options()

chrome_download_dir = r'C:\Users\jackr\Desktop\projects\nonflowers_pi\selenium-flowergrab\\'
chrome_download_dir = os.getcwd()

chrome_options.add_argument("--headless")
prefs = {'download.default_directory' : chrome_download_dir}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
# # // ChromeDriver is just AWFUL because every version or two it breaks unless you pass cryptic arguments
# //AGRESSIVE: options.setPageLoadStrategy(PageLoadStrategy.NONE); // https://www.skptricks.com/2018/08/timed-out-receiving-message-from-renderer-selenium.html
chrome_options.add_argument("start-maximized")# // https://stackoverflow.com/a/26283818/1689770
chrome_options.add_argument("enable-automation")# // https://stackoverflow.com/a/43840128/1689770
chrome_options.add_argument("--headless")# // only if you are ACTUALLY running headless
chrome_options.add_argument("--no-sandbox")# //https://stackoverflow.com/a/50725918/1689770
chrome_options.add_argument("--disable-infobars")# //https://stackoverflow.com/a/43840128/1689770
chrome_options.add_argument("--disable-dev-shm-usage")# //https://stackoverflow.com/a/50725918/1689770
chrome_options.add_argument("--disable-browser-side-navigation")# //https://stackoverflow.com/a/49123152/1689770
chrome_options.add_argument("--disable-gpu")# //https://stackoverflow.com/questions/51959986/how-to-solve-selenium-chromedriver-timed-out-receiving-message-from-renderer-exc


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

# seems to fail consistently on the first time so we should retry
max_retries = 5
retries = 0
while retries < max_retries:
    try:
        driver.execute_script("makeDownload()")
    except:
        pass

print("waiting to make sure file has downloaded...")
time.sleep(5)
# should be "Welcome to Python.org"
title = driver.title

# close
driver.close()
