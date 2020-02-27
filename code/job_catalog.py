"""
Created on Sun Feb 23 23:32:46 2020

@author: llx
"""
def job_catalog(position_name, driver_name, job_describtions):
	import datetime
	import random
	import time
	print("Crawling Position: {}".format(position_name))

	# visit page
	driver_name.get("https://www.lagou.com/jobs/list_{}/p-city_215?px=default#filterBox".format(position_name))

	# clear the stupid ad
	sb_ad = driver_name.find_element_by_class_name("body-btn")
	if sb_ad.text == '给也不要':
		sb_ad.click()

	# extract data
	page_max = int(driver_name.find_element_by_class_name("page-number").text.split(r"/")[1])
	page_current = 1
	print(page_max)
	print(page_current)

	while page_max >= page_current:

		page_current = int(driver_name.find_element_by_class_name("page-number").text.split(r"/")[0])
		print("***Crawling Page: {}".format(page_current))

		# extract job info
		jobs = driver_name.find_elements_by_class_name("con_list_item")

		job_no = 1
		for job in jobs:
			job_describtion = {}
			print("******Crawling Page {} Row {}...".format(page_current, job_no))

			job_describtion["Path"] = job.find_element_by_class_name("position_link").get_attribute("href")

			job_text = job.text
			job_info = job_text.split("\n")
			print(job_info)

			job_describtion["Title"] = job_info[0]
			job_describtion["Location"] = job_info[1][1:-1]

			job_line1 = job_info[3].replace("/", "").split()
			job_describtion["Income_Range(k)"] = job_line1[0].lower()
			job_describtion["Experience"] = job_line1[1]
			job_describtion["Degree"] = job_line1[2]
			job_describtion["Company"] = job_info[4]

			job_line2 = job_info[5].replace("/", "").split()
			job_describtion["Industry"] = job_line2[0]
			job_describtion["Finance"] = job_line2[1]
			job_describtion["Size"] = job_line2[2]

			job_describtion["Tags"] = job_info[6]
			job_describtion["Highlights"] = job_info[7]

			# system datetime
			job_describtion["Sys_Date"] = datetime.datetime.now().strftime("%Y%m%d")
			job_describtion["Sys_Time"] = datetime.datetime.now().strftime("%H:%M:%S")

			# added datetime
			add_datetime = job_info[2]
			if ":" in add_datetime:
				job_describtion["Add_Date"] = job_describtion["Sys_Date"]
				job_describtion["Add_Time"] = add_datetime[0:5]
			elif "天前发布" in add_datetime:
				job_describtion["Add_Date"] = (datetime.datetime.now() - datetime.timedelta(days=int(add_datetime.replace("天前发布","")))).strftime("%Y%m%d")
				job_describtion["Add_Time"] = "00:00"
			else:
				job_describtion["Add_Date"] = datetime.date.fromisoformat(add_datetime).strftime("%Y%m%d")
				job_describtion["Add_Time"] = "00:00"

			print(job_describtion)

			job_describtions.append(job_describtion)
			job_no += 1

		if page_max <= page_current:
			break

		# next page
		driver_name.find_element_by_class_name("pager_next").click()

		# random sleep
		sleep_time = random.randrange(10, 20)
		print("***Sleeping Time: {}".format(sleep_time))
		time.sleep(sleep_time)
	return 1

