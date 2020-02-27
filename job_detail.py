"""
Created on Mon Feb 24 23:40:07 2020

@author: llx
"""

def job_detail(job_data, detail_driver, job_details, start_num):
	import random
	import time

	total_job = len(job_data["Path"])
	cnt = 1
	for job_path in zip(job_data["Path"]):

		if cnt < start_num:
			cnt += 1
			continue

		job_detail = {}

		print("Crawling {} / {}".format(cnt, total_job))
		print()

		detail_driver.get(job_path[0])

		job_detail["No"] = cnt

		job_detail["Path"] = job_path[0]
		job_detail["Advantage"] = detail_driver.find_element_by_class_name("job-advantage").text.replace("职位诱惑：\n", "")
		job_detail["Description"] = detail_driver.find_element_by_class_name("job-detail").text
		job_detail["Address"] = detail_driver.find_element_by_class_name("job-address").text.replace("工作地址\n", "")[:-8]

		print(job_detail)

		job_details.append(job_detail)

		sleep_time = random.randrange(20, 40)
		print("###Sleeping Time: {}s".format(sleep_time))
		time.sleep(sleep_time)

		cnt += 1