# !/usr/bin/env/python
# -*- coding: utf-8 -*-
# @Time : 2023/5/19 15:10
# Author : zhaoning
# File : run.py.py
from file_load import read_by_colums
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

ip = input('请输入ip地址：\n')
name = input("请输入登录的用户名：\n")
password = input("请输入登录密码：\n")

def get_url():
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(f'http://{ip}')
    driver.maximize_window()
    driver.implicitly_wait(5)
    ele_info = '[placeholder="请输入用户名"]'
    driver.find_element(By.CSS_SELECTOR,ele_info).send_keys(name)
    ele_info = '[placeholder="请输入密码"]'
    driver.find_element(By.CSS_SELECTOR,ele_info).send_keys(password)
    ele_info = '//*[text()="登 录"]'
    driver.find_element(By.XPATH,ele_info).click()
    sleep(2)
    try:
        ele_info = '//*[contains(text(),"取消")]'
        driver.find_element(By.XPATH,ele_info).click()
    except:
        pass
    finally:
        sleep(1)
        return driver

def run():
    driver = get_url()
    # print(ip)
    uuids = read_by_colums('uuid', 'bc_data.csv')
    for i in range(len(uuids)):
        url = f'http://{ip}/page/mg/admin/topology-management/edit/{uuids[i]}'
        driver.get(url)
        ele_info = '//*[text()="确定"]'
        driver.find_element(By.XPATH,ele_info).click()
        sleep(1)

    driver.close()

run()