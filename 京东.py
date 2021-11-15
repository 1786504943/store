from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"http://jd.com")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='key']").send_keys("华为p40")
time.sleep(1)
driver.find_element_by_xpath("//*[@class='button']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@width='220']").click()
data=driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[4]/div[22]/a[2]").click()





