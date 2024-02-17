import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = None

def turn_screen_black():
    # Move mouse cursor to the corner to hide it
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width, screen_height)

    # Turn off the screen using xset command (requires xset package)
    subprocess.run(["xset", "dpms", "force", "off"])


import pyautogui

def turn_screen_on():
    # Move mouse cursor to the center of the screen
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2, screen_height / 2)


def chrome_init():
    global driver
    chrome_driver_path = '/path/to/chromedriver'
    # Create a new Chrome session
    service = Service(chrome_driver_path)
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Optional: run Chrome in headless mode (without GUI)
    driver = webdriver.Chrome(service=service, options=chrome_options)

def open_borwser(url):
    driver.get(url)

def close_browser():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
    driver.quit()

