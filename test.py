# %%from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException

import urllib
from time import sleep
# str(raw_input("Enter the message:\n"))
# display = Display(visible=0, size=(800, 600))
# display.start()
driver = webdriver.Chrome()

phone = ['9514786321','123456789','987654321']                  #enter comma separated strings with 10 digit phone numbers or read them from a file
msg = "Thank you for your response. Welcome aboard!"            #message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys

msg = urllib.quote(msg)                                         #url-encode the message, use other functios for handling dictionaries, not recommended
driver.get('https://web.whatsapp.com')                          #first call without delay in order to scan qr code
for i in range(len(phone)):
    url='https://web.whatsapp.com/send?phone=91' + phone[i] + "&text=" + msg
    print url
    driver.get(url)
    sleep(5)
    try:
        driver.find_element_by_css_selector('#main > footer > div._3pkkz.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text').send_keys(Keys.RETURN)
        sleep(5)
    except UnexpectedAlertPresentException:                     #handles stupid popup asking if you really want to leave the page
        pass