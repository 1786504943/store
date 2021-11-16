
'''

注册
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver =webdriver.Chrome()
driver.get(r"http://8.129.91.152:8765/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/span[1]/a").click()
driver.find_element_by_xpath("//*[@id='phone']").send_keys("15711975009")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click()
driver.find_element_by_xpath("//*[@name='password']").send_keys('20000429xuhao')
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]/a[2]").click()
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a/img").click()     #  实名认证
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[1]/div/input").send_keys("于德懋")
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[2]/div/input").send_keys("140624198109227411")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[3]/div/button").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[4]/a").click() # 修改密码
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[1]/input").send_keys("20000429xuhao")
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[2]/input").send_keys("123456xuhao")
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[3]/input").send_keys("123456xuhao")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[5]/button[1]").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[2]/a").click()   #添加银行卡
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/a").click()

ele=driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/form/div[2]/div/select")
st=Select(ele)
st.select_by_index(4)
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/form/div[3]/div/input").send_keys("6227007201360049787")

ele1=driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/form/div[4]/div/div[1]/select")
st1=Select(ele1)
st1.select_by_index(5)
time.sleep(2)
ele2=driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/form/div[4]/div/div[2]/select")
st2=Select(ele2)
st2.select_by_index(5)

driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/form/div[5]/div/input").send_keys("昌平支行")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/form/div[6]/div/button").click()

