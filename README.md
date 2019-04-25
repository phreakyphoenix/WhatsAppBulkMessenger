# WhatsApp Bulk Messager :mega:

## :dart: What it does 
This tool makes adding multiple people to a whatsapp group much easier. 

To prevent spam, WhatsApp desn't allow users to add anyone who is not there in their contact list to a group. So one has to either send them the group link over email etc., which might not be seen by them immediately. 

This tool allows you to directly send the link to a list of people who can instantly join your group. :tada:

## :rocket: Getting Started 

### :runner: Basic installation guide

You may consider using `virtualenv <http://pypi.python.org/pypi/virtualenv>` to create isolated Python environments.

1. `Git clone` this proect from your terminal or download the zip from Github web.
2. activate your virtual environment if you made one, using 
  `source <venv dir>/activate`
3. `cd` to the project folder.
4. Install the requirements using `pip install -r requirements.txt`
5. Open the file `run.py` and update the variable `msg` with the message you want to send to all the numbers.
6. Update the variable `phone` with a comma separated list of phone numbers (option 1).
7. Additionally, you can make a file called `numbers.txt` whcih will store all the 10 digit numbers line by line (option 2).
8. Execute the file `run.py`.

