from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clickelement(driver, locator, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator)).click()
    except Exception as e:
        print(f"Error whie clicking on the element {e}")

