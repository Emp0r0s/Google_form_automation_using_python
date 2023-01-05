#imports
from selenium import webdriver
import time


web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/e/1FAIpQLScMNAMFQd9IJLd4s1YwPYsv5ckogWP24ptkU1Jhwizn8XMD3g/viewform?vc=0&c=0&w=1&flr=0") #------> url of the form

time.sleep(5)

#form fillup
name = input("Name : ")
name_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_field.send_keys(name)

email = input("Email : ")
email_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys(email)

address = input("Address : ")
address_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
address_field.send_keys(address)

p_no = input("p_no : ")
p_no_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
p_no_field.send_keys(p_no)

comments = input("comments : ")
comments_field = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
comments_field.send_keys(comments)

#submission of form
submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()
time.sleep(1)

#Exception handling
try:
    thank_you_message = web.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div/div[3]")
    print("Form submitted successfully")
except Exception as NoSuchElementException:
    print("Form submission failed ........ " , NoSuchElementException )