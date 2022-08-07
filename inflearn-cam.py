from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

username = 'alzpqm@naver.com'
password = '(dlsgur)0622'
target_course_url = 'https://www.inflearn.com/course/%EC%8A%A4%ED%94%84%EB%A7%81-%ED%95%B5%EC%8B%AC-%EC%9B%90%EB%A6%AC-%EA%B8%B0%EB%B3%B8%ED%8E%B8/unit/55327?tab=curriculum'

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.inflearn.com/")
driver.maximize_window()

sleep(3)
driver.find_element(By.XPATH, '//*[@id="header"]/nav/div[2]/div/div[2]/div[2]/div[2]/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/article/form/div/input').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/article/form/div/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/article/form/button').click()

sleep(3)
driver.get(target_course_url)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div/div[1]/div[3]/div[2]/button[4]').click()

sleep(2)
if driver.find_element(By.XPATH,
                       '//*[@id="root"]/main/div/div/div[1]/div/div[1]/div[3]/div[2]/button[1]').accessible_name == '재생':
    driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div/div[1]/div[3]/div[2]/button[1]').click()
while (True):
    sleep(3)
    if driver.find_element(By.XPATH,
                           '//*[@id="root"]/main/div/div/div[1]/div/div[1]/div[3]/div[2]/button[1]').accessible_name == '재생':
        driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div/div[1]/div[3]/div[2]/button[1]').click()
    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div/div[1]/div/div[4]/div/div/div[3]/button[2]').click()
    except:
        pass
