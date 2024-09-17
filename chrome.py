from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading

RICKROLL_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

chrome_options = Options()
# these options make sure chrome doesnt close tabs or try to save memory
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument("--disable-backgrounding-occluded-windows")
chrome_options.add_argument("--disable-renderer-backgrounding")
chrome_options.add_argument("--disable-site-isolation-trials")
chrome_options.add_argument("--max-unused-resource-memory-usage-percentage=100")
chrome_options.add_argument("--force-fieldtrials=TabGroups-TabRestore_DoesNotUnfreezeBackgroundTabs/Enabled/")
chrome_options.add_argument("--disable-features=TabFreeze,TabGroups,AutomaticTabDiscarding")
chrome_options.add_argument("--memory-pressure-thresholds=4")

driver = webdriver.Chrome(options=chrome_options) # create the chrome driver

running = True

def open_tabs(iterations: int = 100): # change 100 if you need more or less tabs
    global running
    counter = 0
    for _ in range(iterations):
        if running:
            driver.execute_script(f"window.open('{RICKROLL_LINK}', '_blank');") # opens a new tab
            counter += 1 # add 1 to the counter
            print(f'Tabs open: {counter}') # display the counter
            time.sleep(0)  # no pause whatsoever
    while True: # keep active until termination
        if running:
            time.sleep(0.1)

def main():
    thread = threading.Thread(target=open_tabs, args=(), daemon=True)
    thread.start()
    thread.join()

if __name__ == '__main__':
    try:
        time.sleep(6)
        main()
    except KeyboardInterrupt: # if we exit the program
        running = False
    finally:
        driver.quit()
