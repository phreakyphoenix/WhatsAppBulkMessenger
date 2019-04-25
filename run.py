from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
import urllib
from time import sleep

# %%from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

driver = webdriver.Chrome()

phone = []                                                      #enter comma separated 10 digit phone numbers here or read them from the numbers_file
with open ('numbers.txt') as numbers_file:
    for line in numbers_file:
        phone.append(str(line))

msg = "3Thank you for your response. Welcome aboard!"            #message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys

msg = urllib.quote(msg)                                         #url-encode the message, use other functios for handling dictionaries, not recommended
driver.get('https://web.whatsapp.com')                          #first call without delay in order to scan qr code
css_selector = '#main > footer > div._3pkkz.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text'

for i in range(len(phone)):
    url='https://web.whatsapp.com/send?phone=91' + phone[i] + "&text=" + msg
    print url
    driver.get(url)
    sleep(4)
    for i in range(100):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            break
        except:
            print("not yet")
            sleep(1)
