import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r"https://www.bilibili.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='primaryChannelMenu']/span[10]/div/a/span").click()
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[2]/div/div[1]/a/div[1]/img").click()
data=driver.window_handles
driver.switch_to.window(data[1])
time.sleep(15)
driver.find_element_by_xpath("//*[@id='bilibiliPlayer']/div[1]/div[2]/div/div[2]/div[1]/input").click()


