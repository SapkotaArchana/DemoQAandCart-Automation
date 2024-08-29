# print the number of elements that has classname = product-thumb
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demo-opencart.com/")

elements = driver.find_elements(By.CLASS_NAME,"product-thumb")
print(f"Number of elements with class name 'product-thumb': {len(elements)}")
# for index, element in enumerate(elements, start=1):
#         print(f"{index}. {element.text}")
#         time.sleep(1)


time.sleep(10)
driver.quit()