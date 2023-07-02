# selenium_test

bash commands for install:
```
sudo apt update
sudo apt install python3.9
sudo apt -y install python3-pip
cd *full folder direction like /home/oem/selenium_test*
source venv/bin/activate
pip install -r requirements.txt
```
Then create .env file in project folder and write in your chat bot token:
```
TELEGRAM_TOKEN=6052918542:AAGuPI_QrqwoaWODNQf5sT9F7oRvwDMlbuc
```

Your can get you bot token in Telegram using telegram bot @BotFather using commands:
```
/start
/newbot
*Name of bot*
*@Id_name_of_bot*
```
You will find your token in messege of BotFather after string 'Use this token to access the HTTP API:'

To start bot use this commands:
```
cd *full folder direction like /home/oem/selenium_test*
source venv/bin/activate
python3 site_checker_bot.py
```
