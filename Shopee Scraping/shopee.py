#shopee.py

from selenium import webdriver #use selenium
from selenium.webdriver.common.keys import Keys # use to enter button send_keys(Keys.RETURN)
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook # save to excel file
import time

# get Email , Password
username = '' #input your email to login shopee
password_1 = '' #input your password to login shopee

def shopeeShop(keyword='หูฟังไร้สาย'):
	driver = webdriver.Chrome() # use Chrome browser
	url = 'https://shopee.co.th/'
	driver.get(url) # open url

	time.sleep(2) #waiting time

	thaiBtn = driver.find_element_by_css_selector('button.shopee-button-outline.shopee-button-outline--primary-reverse').click()
	loginBtn = driver.find_element_by_css_selector('li.navbar__link.navbar__link--account.navbar__link--tappable.navbar__link--hoverable.navbar__link-text.navbar__link-text--medium').click()
	time.sleep(2)

	loginBtn_1 = driver.find_element_by_css_selector('button._1BMmPI._37G57D._30hdn9').click()

	#input email , password
	EmailText = driver.find_element_by_name('loginKey')
	PassText = driver.find_element_by_name('password')
	EmailText.send_keys(f'{username}')
	PassText.send_keys(f'{password_1}')
	PassText.send_keys(Keys.RETURN) #enter 

	# input to search something
	time.sleep(2)
	search = driver.find_element_by_css_selector('input.shopee-searchbar-input__input')
	search.send_keys(keyword)
	search.send_keys(Keys.RETURN)

	time.sleep(3)
	page_html = driver.page_source # click right to see source 
	# print(page_html)
	data = soup(page_html,'html.parser')
	# print(data)

	Name = data.findAll('div',{'class':'O6wiAW'})
	Price = data.findAll('span',{'class':'_341bF0'})

	NameProduct = []
	PriceProduct = []

	for i in Name:
		NameProduct.append(i.text)

	for i in Price:
		PriceProduct.append(i.text)


	print(NameProduct)
	print(PriceProduct)

	# export to excel file
	excelfile = Workbook()
	sheet = excelfile.active

	header = ['ชื่อสินค้า','ราคา']
	sheet.append(header)

	for x,y in zip(NameProduct,PriceProduct):
		sheet.append([x,y])

	excelfile.save(f'Shopee_{keyword}.xlsx')

	# Close web
	time.sleep(3)

	driver.close()

shopeeShop()
