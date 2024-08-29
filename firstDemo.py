import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


firstName = "Archana"
lastName = "Sapkota"
email = "arkanasapkota6@gmail.com"
mobileNum = "98677777777"
gender = "Female"
Current_Address = "Kapan"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/automation-practice-form")


#  Name
driver.find_element(By.ID, "firstName").send_keys(firstName)
driver.find_element(By.ID, "lastName").send_keys(lastName)

#  Email
driver.find_element(By.ID, "userEmail").send_keys(email)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# Gender Radio buttons
driver.find_element(By.XPATH, "//label[normalize-space()='Female']").click()

# Phone Number
driver.find_element(By.ID, "userNumber").send_keys(mobileNum)

# Date of Birth
try:
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(1)  # Wait for the date picker to open
    # Selecting month
    driver.find_element(By.XPATH, "//option[text()='June']").click()
    time.sleep(1)
    # Select the day
    driver.find_element(By.XPATH, "//div[contains(@class,'datepicker__day') and text()='9']").click()
    time.sleep(1)
    print("Date selected successfully.")
except Exception as e:
    print("An error occurred:", e)

# Subjects Dropdown
driver.find_element(By.ID, "subjectsInput").send_keys('m')
time.sleep(1)  # Wait for the autocomplete options to appear
option = driver.find_element(By.XPATH, "//div[contains(@class, 'subjects-auto-complete__option') and text()='Maths']")
option.click()
print("Subject selected")

#  Hobbies Checkbox
element = driver.find_element(By.XPATH, "//label[normalize-space()='Reading']")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

# Picture
pic = driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
file_path = "C:/Users/ArchanaSapkota/Pictures/myphone/Viber/archana.jpg"  # Replace with the actual file path
pic.send_keys(file_path)

#  Current Address
driver.find_element(By.ID,"currentAddress").send_keys(Current_Address)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# State and Cities Dropdown
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Select State')]"))).click()
driver.find_element(By.XPATH, "//div[contains(text(),'NCR')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "city"))).click()
driver.find_element(By.XPATH, "//div[contains(text(),'Delhi')]").click()


# Submit button
try:
    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='submit']")))
    print("Submit button found")
    driver.execute_script("arguments[0].click();", submit_button)
except Exception as e:
    print("Submit button not found:", e)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(10)
driver.quit()

