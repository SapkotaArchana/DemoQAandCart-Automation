# Click on 'Tablets' and assert that the page loaded is tablets (url, title, left navigation, page heading)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://demo-opencart.com/")
time.sleep(2)

try:
    tablets_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link'][normalize-space()='Tablets']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tablets_link)
    driver.execute_script("arguments[0].click();", tablets_link)

#  Assert using URL
    assert driver.current_url == "https://demo-opencart.com/index.php?route=product/category&language=en-gb&path=57", f"URL does not match expected: {driver.current_url}"
    print("URL assert done.")

# using title
    assert driver.title == "Tablets", f"Page title does not contain 'Tablets': {driver.title}"
    print("Title assert done.")

# using title
    left_nav = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "column-left")))
    active_item = left_nav.find_element(By.CSS_SELECTOR, ".list-group-item.active")

    assert "Tablets" in active_item.text, f"Left navigation column is not present : {active_item.text}"
    # assert left_nav is not None is to check that the left navigation column is present on the page.
    # assert left_nav is not None, "Left navigation column is not present" # overall left nav hereko ho
    print("Left navigation assertion done.")

# using page Heading
    page_heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h2"))
    )
    assert "Tablets" in page_heading.text, f"Page heading does not contain 'Tablets': {page_heading.text}"
    print("Page heading assertion passed.")

except Exception as e:
    print("Tablets not found:", e)

time.sleep(10)
