# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# set driver

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5501/")

# functions

# test1()
def elementOne ():
    elementOne = driver.find_element(By.ID, value="element-one")
    elementOne.click()
elementOne()
driver.save_screenshot("elementOne.png")

time.sleep(0.1)
# test2()
def elementTwo ():
    elementTwo = driver.find_element(By.ID, value="element-two")
    ActionChains(driver).double_click(elementTwo).perform()
elementTwo()
driver.save_screenshot("elementTwo.png")

time.sleep(0.1)
# test3()
def elementThree ():
    elementThree = driver.find_element(By.ID, value="element-three")
    ActionChains(driver).move_to_element(elementThree).perform()
elementThree()
driver.save_screenshot("elementThree.png")
time.sleep(0.1)

# test4()
def elementFour ():
    elementFour = driver.find_element(By.ID, value="element-four")
    elementFour.click()
elementFour()

driver.save_screenshot("elementFour.png")
time.sleep(0.1)

# test5()
def input_Field ():
    input_Field = driver.find_element(By.ID, value="myInput")
    input_Field.send_keys("teszt")
input_Field()
driver.save_screenshot("inputField.png")
time.sleep(0.1)

print("teszt jo")
driver.close()