from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.saucedemo.com/"

driver = webdriver.Firefox()
# Open the webpage to url
driver.get(url)
sleep(2)

#maximise window
driver.maximize_window()

#input some txt in the username field & Password
webelement_of_email_input = driver.find_element(By.ID,"user-name")
webelement_of_email_input.send_keys("standard_user")

webelement_of_password_input = driver.find_element(By.ID,"password")
webelement_of_password_input.send_keys("standard_user")

#click login button
webelement_of_login_button= driver.find_element(By.ID, "login-button")
webelement_of_login_button.click()
#title of page
print(driver.title)
#get page source
page_content = driver.page_source
#save the entire content of webpage
with open("Webpage task 11.txt", "w") as file:
    file.write(page_content)
print(page_content)

