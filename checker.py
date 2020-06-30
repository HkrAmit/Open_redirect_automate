import requests, time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

links=open("payloaded.txt","r").readlines()

options=Options()
options.headless=True
browser=webdriver.Firefox(options=options, executable_path = r'/root/Desktop/Automation/HedlessBrowser/Bin/geckodriver')
#link='http://www.fa3.in/search/redirect?Url=https://google.com&num=421&title=E-Tender%20Portal'

for link in links:
    browser.get(link)
    try:
        alert=browser.switch_to_alert()
        if alert:
            alert.accept()
    except:
        pass

    time.sleep(5)
    if browser.current_url.find("https://www.openbugbounty.org/")==0
        print("success")
    else:
        print("No")
browser.quit()
