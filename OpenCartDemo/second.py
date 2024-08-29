# print the names of menu having class 'nav-item'.\
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://demo-opencart.com/")

menu_items = driver.find_elements(By.CLASS_NAME, "nav-item")
elements_name = [items.text for items in menu_items]
print(f"Number of menu items with class name 'nav-item': {len(menu_items)}")

# for index, item in enumerate(menu_items, start=1):
#     print(f"{index}. {item.text}")
#     time.sleep(0.50)
for names in elements_name:
        print(names)

driver.quit()  
