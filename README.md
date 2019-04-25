# WhatsApp Bulk Messager :loudspeaker:

## :dart: What it does 
This tool makes adding multiple people to a whatsapp group much easier. 

To prevent spam, WhatsApp desn't allow users to add anyone who is not there in their contact list to a group. So one has to either send them the group link over email etc., which might not be seen by them immediately. 

This tool allows you to directly send the link to a list of people who can instantly join your group. :tada:

## :rocket: Getting Started 

### :walking: Basic installation 

You may consider using `virtualenv <http://pypi.python.org/pypi/virtualenv>` to create isolated Python environments.

1. `Git clone` this proect from your terminal or download the zip from Github web.
2. Activate your virtual environment if you made one, using 
  `source <venv dir>/activate`
3. `cd` to the project folder.
4. Install the requirements using `pip install -r requirements.txt`

### :iphone: Adding Phone Numbers

You may use any or all of the following methods to enter the mobile numbers

1. When you execute `run.py`, you can enter any number of comma separated 10 digit phone numbers at the prompt at once.
2. Update the variable `phone` with a comma separated list of phone numbers
3. Make a file called `numbers.txt` whcih will store all the 10 digit numbers, each on a line. To use thi feature comment out the three commented lines in `run.py` for input from file.

### :running: Running

1. Open the file `run.py` and update the variable `msg` with the message you want to send to all the numbers.
2. Make sure you've added the numbers properly. Make sure there are no duplicates.
3. Execute the file `run.py` and go grab a :coffee:
