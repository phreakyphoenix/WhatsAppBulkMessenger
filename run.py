from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import quote
from time import sleep

# %%from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

driver = webdriver.Chrome()

phone = []                                                      #enter comma separated 10 digit phone numbers here or read them from the numbers_file
with open ('numbers.txt') as numbers_file:
    for line in numbers_file:
        phone.append(str(line))

msg = "Thank you for your response. Check out google.com"           #message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys

msg = quote(msg)                                                #url-encode the message, use other functios for handling dictionaries, not recommended
driver.get('https://web.whatsapp.com')                          #first call without delay in order to scan qr code
css_selector = '#main > footer > div._3pkkz.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text'
sleep(2)
for number in phone:
    url='https://web.whatsapp.com/send?phone=91' + number + "&text=" + msg
    driver.get(url)
    sleep(3)                                                    #any delay is okay, even 0, but 3-5 seems appropriate
    for i in range(100):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            break
        except:
            print("not yet")
            sleep(1)
    print 'Last Number', number
# driver.quit()                                                 #uncomment to close chrome window as scoon as program ends