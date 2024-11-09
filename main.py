import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from speed_enum import TimeLimit

ERROR_RATE = 0.05  # 5% error rate
DELAY = 1  # 1 second delay
TIME_LIMIT = TimeLimit.ONE_MIN

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


def click_element(xpath: str):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


try:
    driver.get("https://teskoran.com")

    # Click through the initial setup
    for xpath in ["//button[text()='PLAY']", f"//label[@for='rd{TIME_LIMIT.value}']", "//label[@for='rdk1']", "//button[text()='OK']", "//button[text()='Mulai']"]:
        click_element(xpath)
        print(driver.find_element(By.XPATH, xpath).text)

    time.sleep(1)

    while driver.find_element(By.CLASS_NAME, "waktu").text != "00:00:00":
        result = sum([int(driver.find_element(By.CLASS_NAME, cls).text) for cls in ["soal1", "soal2"]]) % 10
        driver.find_element(By.TAG_NAME, "body").send_keys(result if random.random() > ERROR_RATE else (result + 1) % 10)
        time.sleep(DELAY)

finally:
    pass
