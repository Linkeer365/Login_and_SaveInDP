# 靠，用pycharm搞github好爽啊...
# https://www.cnblogs.com/feixuelove1009/p/5955332.html

import selenium

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from PIL import Image

# 解决点不动的问题
# https://stackoverflow.com/questions/21350605/python-selenium-click-on-button

from selenium.webdriver.support.ui import WebDriverWait

# 一出现就马上点，这个操作好啊！！！

# https://stackoverflow.com/questions/62868434/button-click-only-works-when-time-sleep-added-for-selenium-python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver import ActionChains

# 怎么写入input框框
# https://stackoverflow.com/questions/18557275/how-to-locate-and-insert-a-value-in-a-text-box-input-using-python-selenium

from selenium.webdriver.common.keys import Keys


import requests

import os
import sys

import time

import yaml

# 别老天天time.sleep了，有更好的pratice！



headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

target_dir=r"D:\AllDowns"
qrcode_name="baidu.png"
qrcode_path=f"{target_dir}{os.sep}{qrcode_name}"

netdisk_link="https://pan.baidu.com/s/1jzwPf888WKCHgLnqQCI50g"
netdisk_passwd="uapr"

results_path=r"D:\AllDowns\results_all.txt"

firefox_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe"

already_path=r"D:\AllDowns\already_save.txt"

if not os.path.exists(already_path):
    open(already_path,"a").close()

# 火狐无头版本
# https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python
# https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
options = Options()
options.headless = True
# options.headless=False

driver=webdriver.Firefox(options=options,executable_path=firefox_path)

max_delay=5

def login():

    login_link="https://pan.baidu.com/"

    driver.get(login_link)

    old_url = driver.current_url

    saoyisaoBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.ID, 'TANGRAM__PSP_4__footerQrcodeBtn')))

    saoyisaoBtn.click()

    time.sleep(1)

    # driver.implicitly_wait(10)

    # 出现二维码之后直接截图扫描，因为它会自己弹窗出来...

    # 想保存的就把注释改正文

    # 出现errno=0(说明登录成功了！)

    driver.save_screenshot(qrcode_path)
    print("qrcode image saved.")

    img=Image.open(qrcode_path)
    img.show()

    # time.sleep(2)

    new_url=driver.current_url

    if "errno=0" in new_url:
        print("login success!")

def write_done_yet(netdisk_link):
    with open(already_path,"a",encoding="utf-8") as f:
        f.write(netdisk_link+"\n")
    print("one written.")

def open_one_link(netdisk_link,netdisk_passwd):
    driver.get(netdisk_link)
    try:
        errorImg=driver.find_element_by_class_name("error-img")
        if errorImg:
            print("bad link!")
            write_done_yet(netdisk_link)
            return None
    except selenium.common.exceptions.NoSuchElementException:
        pass

    # # 因为这个不确定跳到那个页面所以
    # time.sleep(3)

    if netdisk_passwd!="":

        inputBox=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.ID, 'accessCode')))

        # inputBox=driver.find_element_by_id("accessCode")
        inputBox.send_keys(netdisk_passwd)

        time.sleep(1)

        inputBox.send_keys(Keys.ENTER)

        time.sleep(1)

        # 考虑到加载耗时
        # driver.implicitly_wait(9)

        # 先登录在保存网盘好吧...


        # 保存到网盘，按钮

        # 艹这里要睡5s！！！

        # implicitly_wait有点不太顶用啊...

        # time.sleep(2)
    try:
        gouxuanBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'zbyDdwb')))
        gouxuanBtn.click()
    except selenium.common.exceptions.TimeoutException:
        print("第二种页面，无需勾选直接保存！")
        pass
    except selenium.common.exceptions.ElementNotInteractableException:
        print("没渲染完，稍等片刻")
        time.sleep(1)
        gouxuanBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'zbyDdwb')))
        gouxuanBtn.click()





    # gouxuanBtn=driver.find_element_by_class_name("zbyDdwb")
    # gouxuanBtn.click()

    print("gouxuan")

    # time.sleep(2)

    baocundaowangpanBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.XPATH, "//a[@data-button-id='b1']")))

    # baocundaowangpanBtn=driver.find_element_by_xpath("//a[@data-button-id='b1']")

    baocundaowangpanBtn.click()

    # time.sleep(2)

    # 搜就硬搜是我存放【等待下载】的文件夹

    # 父节点获取有两种手段，详见：
    # https://blog.csdn.net/huilan_same/article/details/52541680

    # 因为登录之后会自动呈现（最近搜索，所以不如直接选择最近使用那个节点...）

    # # soujiuyingsouBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.XPATH, "//span[@class='save-chk-io']")))

    # 节点是每次登录（并保存至少一次之后才）更新的，艹！

    soujiuyingsouBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.XPATH, "//span[@node-path='/搜，就硬搜']/parent::span")))

    # soujiuyingsouBtn=driver.find_element_by_xpath("//span[@node-path='/搜，就硬搜']/parent::span")
    soujiuyingsouBtn.click()

    # time.sleep(1)
    quedingBtn=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.XPATH, "//span[@class='text' and text()='确定']")))
    # quedingBtn=driver.find_element_by_xpath("//span[@class='text' and text()='确定']")
    quedingBtn.click()

    yibaocunNode=WebDriverWait(driver,max_delay).until(EC.presence_of_element_located((By.XPATH, "//span[@class='tip-msg']")))

    # driver.close()

    write_done_yet(netdisk_link)

    print("one done.")

def main():

    login()

    with open(results_path,"r",encoding="utf-8") as f:
        lines=f.readlines()

    lines=[each.strip("\n") for each in lines if each!="\n"]

    with open(already_path,"r",encoding="utf-8") as f:
        already_links=set(f.readlines())

    for each in lines:
        each_dict=yaml.load(each)
        link,passwd=each_dict["netdisk_link"],each_dict["passwd"]
        if link+"\n" in already_links:
            continue
        open_one_link(link,passwd)
        time.sleep(5)

    driver.quit()
    print("all down.")

if __name__ == '__main__':
    main()




# print("old url:",old_url)
# print("new url:",new_url)



# time.sleep(2)








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




