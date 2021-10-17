import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_flower():
    """this function is only called when the file is executed directly"""

    print("setting options...")
    chrome_options = Options()

    # this sets the download directory for the flower image to be
    # ...wherever we run the script from
    prefs = {'download.default_directory' : os.getcwd()}
    chrome_options.add_experimental_option('prefs', prefs)

    # this argument tells the browser to run without any gui
    # ...which is essential on the pi zero
    chrome_options.add_argument("--headless")

    # these options are here to stop the timeout bug but do not seem to work
    # ...going to leave them here but comment them in case we need them again
    # chrome_options.add_argument("start-maximized")# // https://stackoverflow.com/a/26283818/1689770
    # chrome_options.add_argument("enable-automation")# // https://stackoverflow.com/a/43840128/1689770
    # chrome_options.add_argument("--headless")# // only if you are ACTUALLY running headless
    # chrome_options.add_argument("--no-sandbox")# //https://stackoverflow.com/a/50725918/1689770
    # chrome_options.add_argument("--disable-infobars")# //https://stackoverflow.com/a/43840128/1689770
    # chrome_options.add_argument("--disable-dev-shm-usage")# //https://stackoverflow.com/a/50725918/1689770
    # chrome_options.add_argument("--disable-browser-side-navigation")# //https://stackoverflow.com/a/49123152/1689770
    # chrome_options.add_argument("--disable-gpu")# //https://stackoverflow.com/questions/51959986/how-to-solve-selenium-chromedriver-timed-out-receiving-message-from-renderer-exc


    # make sure to install the driver first and put
    # ...it in the same directory
    print("initialising driver...")
    driver = webdriver.Chrome(options=chrome_options)

    # load the webpage
    print("loading webpage...")
    # although this will timeout - it seems that
    # ...enough of the page does load for it to not matter
    # TODO: can we make this timeout sooner? or finish on loading the element we care about?
    # ...this could save some time (precious on the low power pi)
    try:
        driver.execute_script("makeDownload()")
    except:
        print("timed out - continuing regardless")

    # this runs the `makeDownload()` function from index.js
    # ...which downloads the flower image locally
    driver.execute_script("makeDownload()")

    print("waiting to make sure file has downloaded...")
    time.sleep(5)
    # should be "Welcome to Python.org"
    title = driver.title

    # close
    driver.close()

if __name__ == "__main__":
    get_flower()