import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from fake_useragent import FakeUserAgent
import time
from PIL import ImageGrab

URL = 'https://offline-dino-game.firebaseapp.com/'

ua = FakeUserAgent()
user_agent = ua.random
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get(url=URL)
driver.maximize_window()

time.sleep(2)

start_game = driver.find_element(By.CLASS_NAME, 'runner-container')

action = ActionChains(driver)
action.move_to_element_with_offset(start_game, 10, 10)
action.click()
action.perform()
action.send_keys(Keys.SPACE)
action.perform()
time.sleep(2)

is_on = True

start_time = time.time()

while is_on:
    img = ImageGrab.grab(bbox=(0, 200, 900, 800))
    arr = np.array(img)
    value_list_1 = ['#%02x%02x%02x' % tuple(i) for i in arr[370][473:493]]
    value_list_2 = ['#%02x%02x%02x' % tuple(i) for i in arr[460][473:493]]
    if value_list_1.count('#ffffff') != 20 or value_list_2.count('#ffffff') != 20:
        action.send_keys(Keys.DOWN)
        action.perform()
        start_time = time.time()
    else:
        end_time = time.time()
        if end_time - start_time > 6:
            action.send_keys(Keys.SPACE)
            action.perform()
            start_time = time.time()
        else:
            continue
        continue

