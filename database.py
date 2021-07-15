
# python 3.6

# (1)	首先打开相应的网页，代码如下
from splinter import Browser
from selenium.webdriver.chrome.options import Options
import os
import time

#========================================================================================================
# function 
def selectdata(genename):	
	chrome_options = Options()
	chrome_options.add_argument("--disable-software-rasterizer")
	browser = Browser(driver_name='chrome',options=chrome_options)
	gene = genename.rstrip('\n')
	url = 'https://www.cbioportal.org/results/mutations?cancer_study_list=nsclc_tcga_broad_2016&tab_index=tab_visualize&case_set_id=nsclc_tcga_broad_2016_all&Action=Submit&gene_list=' + gene
	browser.visit(url)
	time.sleep(20)
	print("open websiete done!")
	# find drop button
	while True:
		if len(browser.find_by_id("addColumnsDropdown")) ==1:
			button = browser.find_by_id("addColumnsDropdown")
			button.click()
			break
	time.sleep(2)
	# click select all button
	button2 = browser.find_by_value("Select all (28)")
	button2.click()
	time.sleep(5)
	# find copy button and copy 
	button3 = browser.find_by_id("copyButton")
	button3.click()
	time.sleep(20)
	# copy data 
	while True:
		if len(browser.find_by_id("modalCopyButton")) ==1:
			button4 = browser.find_by_id("modalCopyButton")
			button4.click()
			break
	time.sleep(5)
	print("Copy data to clipboard done!")
	# save data 
	import win32clipboard as w
	import win32con
	w.OpenClipboard()
	d = w.GetClipboardData(win32con.CF_TEXT)
	w.CloseClipboard()
	s = d.decode('GBK')
	#print(s)
	resfile="D:/BIT_database/" + gene +".txt"
	f = open(resfile, 'w')
	f.write(s)
	f.close()
	browser.quit()
	time.sleep(10)





# main 
for line in open("D:/BIT_database/genelist.txt", "r", encoding="utf-8"):
	filelist = os.listdir("D:/BIT_database")
	filename = line.rstrip('\n') + ".txt"
	if not filename in filelist:
		selectdata(line)



























