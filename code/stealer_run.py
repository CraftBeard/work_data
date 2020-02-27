#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:13:49 2020

@author: llx
"""

# Import libraries
import time
import datetime
import pandas as pd
import random
import sys
from selenium import webdriver
sys.path.append(r"/Users/llx/PyProjects/job_wizard/job_stealer")
from job_catalog import job_catalog
from job_detail import job_detail

# Set Parameters
position_name = input("1.数据分析师\n2.金融数据分析师\n3.风险分析师\n请选择：")
if position_name == "1":
	position_name = "数据分析师"
elif position_name == "2":
	position_name = "金融数据分析师"
elif position_name == "3":
	position_name = "风险分析师"
print("正在爬取：{}".format(position_name))

yyyymmdd = datetime.datetime.now().strftime("%Y%m%d")

profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.image", 2)

# Main Programs
## Get overview list of jobs
catalog_driver = webdriver.Firefox(firefox_profile=profile)
job_describtions = []
job_catalog(position_name, catalog_driver, job_describtions)
catalog_driver.quit()

# Save Data
job_data = pd.DataFrame(job_describtions)
file_name = "/Users/llx/PyProjects/job_wizard/" + position_name + "_汇总_" + yyyymmdd + ".csv"
job_data.to_csv(file_name, index=False)

## Get details of jobs
job_data = pd.read_csv(file_name)
start_page = 1
detail_driver = webdriver.Firefox(firefox_profile=profile)
job_details = []
job_detail(job_data, detail_driver, job_details, start_page)
detail_driver.quit()

## Save Data
job_details_tb = pd.DataFrame(job_details)
file_name = "/Users/llx/PyProjects/job_wizard/" + position_name + "_明细_" + yyyymmdd + ".csv"
if start_page == 1:
	job_details_tb.to_csv(file_name, index=False)
else:
	job_details_tb.to_csv(file_name, index=False, mode='a', header=False)


## Data preprocessing


# Save Data
## Upload github

## Local