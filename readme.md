

## Simple Whatsapp Bot

Send automatized messages to your contact list at an specific hour and birthday messages in their special day.

## How to install
*First of all Download Chrome and connect your Whatsapp account on it

* Copy the file in your repository

    git clone https://github.com/Ulysses-Alv/WppBot.git
* Install the requirements

    pip install -r requirements.txt
## How to send automatized Messages

* Open GUI to create your message. (tip: check automatizedMessage.json if your message was succesfully created):

    py _GUIMessage.py

* Execute _onTimeSender.py:

    py _onTimeSender.py

* It's ready. It will send the message at the hour you said.
Remember: You have to delete it or it will send the message again the next day.

## How to send birthday messages.
* Open GUI to create your message. (tip: check birthdays.json if your message was succesfully created):

    py _GUIBirthday.py
* **In Windows:** 
* go to task scheduler
* Create new task
* name it as you want
* select the exec.bat file with 
* `py _birthdayBot.py`
* In triggers; add
* new trigger: dialy. and pick when you want to execute it.
* Done.
[See this video if you have any doubts](https://www.youtube.com/watch?v=s_EMsHlDPnE)
## Limitations

 - You need to register your Whatsapp account with QR
 - Only works with your contacts that are not archived.
 - Only support UTF-8: if your contact has emojis or ñ, it won't work.

 
