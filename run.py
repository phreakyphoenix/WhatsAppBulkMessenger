from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Uncomment line below to use python 2
# from urllib import quote   

#Uncomment line below to use python 3 
from urllib.parse import quote

from time import sleep
# %%from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

driver = webdriver.Chrome()

phone = []                                                      #enter comma separated 10 digit phone numbers here or read them from the numbers_file
with open ('numbers.txt') as numbers_file:                    #uncomment these three three lines to read input from numbers.txt file
    for line in numbers_file:
    	line=line.strip()
    	if len (line)==10:								   		#skip if you have no empty lines
    		phone.append(str(line))

# phone.extend(str(raw_input("Enter the comma separated list of numbers (Press enter to skip)\n")).split(','))

# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''
Hey!!
This is a *test* _message_.
See you can do _*all sorts of text formatting*_.
You can join my fancy group to lear ML at https://whatsapp.com/amazingML
'''     

msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended
driver.get("https://web.whatsapp.com")  # first call without delay in order to scan qr code
css_selector = "#main > footer > div._3pkkz.V42si.copyable-area > div._1Plpp > div > div._2S1VP.copyable-text.selectable-text"
sleep(2)
for number in phone:
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    sleep(3)  # any delay is okay, even 0, but 3-5 seems appropriate
    for i in range(100):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            break
        except:
            print("not yet")
            sleep(1)
    print ('Last Number '+ str(number))
print ("Done")
# driver.quit()                                                 #uncomment to close chrome window as scoon as program ends
