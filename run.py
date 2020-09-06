from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# from urllib import quote      #Uncomment line below to use python 2
from urllib.parse import quote  #Uncomment line below to use python 3 

from time import sleep
# %%from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

#update css selector if you have any issues
css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"

# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''
You can try all sorts of formatting like _italics_ and *bold* or _*bold italics*_. 

Multiline works too.

And so do links like https://google.com!
'''     

driver = webdriver.Chrome()

phone = []                                                      #enter comma separated 10 digit phone numbers here or read them from the numbers_file
with open ('numbers.txt') as numbers_file:                    #uncomment these three three lines to read input from numbers.txt file
    for line in numbers_file:
    	line=line.strip()
    	if len (line)==10:								   		#skip numbers of length not equal to 10
    		phone.append(str(line))
# phone.extend(str(raw_input("Enter the comma separated list of numbers (Press enter to skip)\n")).split(','))

msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended
driver.get("https://web.whatsapp.com")  # first call without delay in order to scan qr code
sleep(2)
failed_list = []
for index, number in enumerate(phone, 1):
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    TRIES = 20

    sleep(3)  # any delay is okay, even 0, but 3-5 seems appropriate
    for i in range(TRIES):
        try:
            driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
            driver.execute_script("window.onbeforeunload = function() {};")
            print (f'Sent to {index} : {number}')
            break
        except:
            print("not yet")
            sleep(1)
        
    else:
        failed_list.append(number)
    
print ("Done")

if (len(failed_list)==0):
    print (f'Message successfully sent to all {len(phone)} numbers.')
else:
    print (f'Message sent to all numbers EXCEPT:')
    for number in failed_list:
        print (number)
    
driver.quit()                                                 #uncomment to close chrome window as scoon as program ends
