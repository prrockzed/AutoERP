# importing packages and libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# opening the file and reading data from it
# also removing the last character(\n) from the data
file = open("yourInfo.txt", "r")
roll = file.readline()
roll = roll[:-1]
pwd = file.readline()
pwd = pwd[:-1]
securityQuestion1 = file.readline()
securityQuestion1 = securityQuestion1[:-1]
answer1 = file.readline()
answer1 = answer1[:-1]
securityQuestion2 = file.readline()
securityQuestion2 = securityQuestion2[:-1]
answer2 = file.readline()
answer2 = answer2[:-1]
securityQuestion3 = file.readline()
securityQuestion3 = securityQuestion3[:-1]
answer3 = file.readline()
answer3 = answer3[:-1]
file.close()
print('Data read successfully')


# opening teh browser
browser = webdriver.Chrome()
browser.get("https://erp.iitkgp.ac.in/")
print('Chrome browser opened')
browser.maximize_window()
browser.implicitly_wait(20)
browser.find_element(By.ID, "user_id").send_keys(roll, Keys.TAB)
browser.implicitly_wait(20)
browser.find_element(By.ID, "password").send_keys(pwd, Keys.TAB)
time.sleep(1.2)
question = browser.find_element(By.ID, "question")


# getting the security questions
try:
    string = question.get_attribute("textContent")
    # string = question.get_attribute("innerHTML")  # -- another way
except Exception as e:
    print("No text content", e)
    exit()


# matching the security question, answering it and login
if string == securityQuestion1:
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(answer1)
    browser.find_element(By.ID, "loginFormSubmitButton").click()
elif string == securityQuestion2:
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(answer2)
    browser.find_element(By.ID, "loginFormSubmitButton").click()
elif string == securityQuestion3:
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(answer3)
    browser.find_element(By.ID, "loginFormSubmitButton").click()
else:
    print("No matching security question found")
    exit()

print('Login successful')


# closing the browser by taking an input
input()
