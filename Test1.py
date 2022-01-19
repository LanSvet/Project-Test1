from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("c:\webdriver\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@href='/upload']").click()

driver.find_element(By.ID, 'file-upload').send_keys("C:/Photo/Anamorphic-Pro-Visual-Effects-Mac-Bundle.jpg")
time.sleep(1)
driver.find_element(By.ID, "file-submit").click()
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.find_element(By.XPATH, "//*[@href='/download_secure']").click()
driver.find_element(By.XPATH, "//*[@href='download_secure/Anamorphic-Pro-Visual-Effects-Mac-Bundle.jpg']").click()
time.sleep(1)

driver.get("http://the-internet.herokuapp.com/")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.find_element(By.XPATH, "//*[@href='/shifting_content']").click()
driver.find_element(By.XPATH, "//*[@href='/shifting_content/menu']").click()
driver.back()

time.sleep(2)
driver.find_element(By.XPATH, "//*[@href='/shifting_content/image']").click()
driver.back()

time.sleep(2)
driver.find_element(By.XPATH, "//*[@href='/shifting_content/list']").click()
driver.back()


driver.quit()
