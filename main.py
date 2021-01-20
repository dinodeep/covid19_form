from splinter import Browser
from getpass import getpass
import time

# get password
try :
    username = "userid"
    password = getpass(prompt = "Password: ")
except :
    print("PASSWORD ERROR")

# initialize browser
browser = Browser("chrome")

# go to form website
browser.visit("https://daily-student.cmu.edu/")

# login
browser.find_by_xpath('//*[@id="username"]').fill(username)
browser.find_by_xpath('//*[@id="passwordinput"]').fill(password)
browser.find_by_xpath('//*[@id="formwrapper"]/div[4]/input').click()

# wait for loading
time.sleep(0.5)

# send 2FA push --> button xpath is inside iframe so need to use id iframe (called 'duo_iframe') and search within iframe
with browser.get_iframe('duo_iframe') as iframe :
    iframe.find_by_xpath('//*[@id="auth_methods"]/fieldset/div[1]/button').click()

# wait for 2FA to be completed
while "Student Daily Self-Assessment" not in browser.title:
    continue

time.sleep(0.5)

# fill survey 
browser.find_by_xpath('//*[@id="Field12_1"]').click()
browser.find_by_xpath('//*[@id="Field3_1"]').click()
browser.find_by_xpath('//*[@id="Field5_2"]').click()

# submit
browser.find_by_xpath('//*[@id="saveForm"]').click()

# close and close browser
browser.quit()