from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def main():
    driver = webdriver.Chrome()
    driver.get("https://erp.iitkgp.ac.in/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "user_id").send_keys("your_roll", Keys.TAB)
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("your_password", Keys.TAB)
    time.sleep(2)
    question = driver.find_element(By.ID, "question")
    try:
        string = question.get_attribute("textContent")
        print("This is the text content", string)
        string1 = question.get_attribute("innerHTML")
        print("This is the inner HTML", string1)
    except Exception as e:
        print("no text content", e)
        exit()

    if string == "your_question1":
        ans = driver.find_element(By.ID, "answer")
        ans.send_keys("answer1")
        driver.find_element(By.ID, "loginFormSubmitButton").click()
    if string == "your_question2":
        ans = driver.find_element(By.ID, "answer")
        ans.send_keys("answer2")
        driver.find_element(By.ID, "loginFormSubmitButton").click()
    if string == "your_question3":
        ans = driver.find_element(By.ID, "answer")
        ans.send_keys("answer3")
        driver.find_element(By.ID, "loginFormSubmitButton").click()

    input()


main()
