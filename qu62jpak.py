# import selenium

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from PIL import Image

# 解决点不动的问题
# https://stackoverflow.com/questions/21350605/python-selenium-click-on-button
from selenium.webdriver import ActionChains

# 怎么写入input框框
# https://stackoverflow.com/questions/18557275/how-to-locate-and-insert-a-value-in-a-text-box-input-using-python-selenium

from selenium.webdriver.common.keys import Keys

import requests

import os
import sys

import time

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

target_dir=r"D:\AllDowns"
qrcode_name="baidu.png"
qrcode_path=f"{target_dir}{os.sep}{qrcode_name}"

netdisk_link="https://pan.baidu.com/s/1jzwPf888WKCHgLnqQCI50g"
netdisk_passwd="uapr"

firefox_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe"

# 火狐无头版本
# https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python
options = Options()
# options.headless = True
options.headless=True

driver=webdriver.Firefox(options=options,executable_path=firefox_path)

driver.get(netdisk_link)

inputBox=driver.find_element_by_id("accessCode")
inputBox.send_keys(netdisk_passwd)

driver.implicitly_wait(2)

inputBox.send_keys(Keys.ENTER)

# 考虑到加载耗时
# driver.implicitly_wait(9)

# 先登录在保存网盘好吧...



# 保存到网盘，按钮

# 艹这里要睡5s！！！

# implicitly_wait有点不太顶用啊...

time.sleep(5)

old_url=driver.current_url

baocundaowangpanBtn=driver.find_element_by_xpath("//a[@data-button-id='b1']")

baocundaowangpanBtn.click()

time.sleep(5)

saoyisaoBtn=driver.find_element_by_id("TANGRAM__PSP_11__footerQrcodeBtn")
saoyisaoBtn.click()

# driver.implicitly_wait(10)

time.sleep(5)

# 出现二维码之后直接截图扫描，因为它会自己弹窗出来...

# 想保存的就把注释改正文

driver.save_screenshot(qrcode_path)
print("qrcode image saved.")

img=Image.open(qrcode_path)
img.show()

# 出现errno=0(说明登录成功了！)

time.sleep(5)

new_url=driver.current_url

# 搜就硬搜是我存放【等待下载】的文件夹

# 父节点获取有两种手段，详见：
# https://blog.csdn.net/huilan_same/article/details/52541680

soujiuyingsouBtn=driver.find_element_by_xpath("//span[@node-path='/搜，就硬搜']/parent::span")
soujiuyingsouBtn.click()

time.sleep(5)

quedingBtn=driver.find_element_by_xpath("//a[@data-button-id='b15']")
quedingBtn.click()

time.sleep(5)

driver.quit()

print("one done.")



# print("old url:",old_url)
# print("new url:",new_url)



# time.sleep(5)








# driver.quit()



# qrcode_imageNode=driver.find_element_by_class_name("tang-pass-qrcode-img")
# img_link=qrcode_imageNode.get_attribute("src")
#
# print("Img:",img_link)
#
# driver.get(img_link)
# driver.save_screenshot(qrcode_path)

# print("qrcode image saved.")

# scanning

# time.sleep(20)
#
# print(page)
#
# driver.quit()
#
# sys.exit(0)






# with open(qrcode_path,"wb") as f:
#     f.write(driver.get(img_link).content)



# print(driver.find_element_by_xpath("//a[@data-button-id='b1']//text()"))

# sys.exit(0)

# ActionChains(driver).click(baocundaowangpanBtn).perform()

# driver.implicitly_wait(5)
#
# loginBtn=driver.find_element_by_xpath("//a[@node-type='header-login-btn']//@href")
# loginBtn.click()
# # ActionChains(driver).click(loginBtn).perform()
#
#
# driver.implicitly_wait(5)

# quedingBox=driver.find_element_by_id("submitBtn")
# quedingBox.click()



# page=driver.page_source
#
# print(page)

# driver.quit()




