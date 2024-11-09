from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random

options = Options()
options.add_experimental_option("detach", True)

# Set up the WebDriver (replace with the path to your WebDriver if necessary)
driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get("https://teskoran.com")

    # Find the button with the text "PLAY" and click it
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='PLAY']"))
    )
    print(play_button.text)
    play_button.click()

    radio_button_time = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='rd1']"))
    )
    print(radio_button_time.text)
    radio_button_time.click()

    radio_button_key = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='rdk1']"))
    )
    print(radio_button_key.text)
    radio_button_key.click()


    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
    )
    print(ok_button.text)
    ok_button.click()


    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Mulai']"))
    )
    print(start_button.text)
    start_button.click()

    time.sleep(1)

    while driver.find_element(By.CLASS_NAME, "waktu").text != "00:00:00":
        angka1 = int(driver.find_element(By.CLASS_NAME, "soal1").text)
        angka2 = int(driver.find_element(By.CLASS_NAME, "soal2").text)

        result = angka1 + angka2
        if result > 9:
            result = result % 10

        body = driver.find_element(By.TAG_NAME, "body")
        if random.random() > 0.00:  # 95% chance to send the correct result
            body.send_keys(result)
        else:  # 3% chance to send an incorrect result
            body.send_keys((result + 1) % 10)

        time.sleep(0.1)

finally:
    # Close the browser
    # driver.quit()
    pass
