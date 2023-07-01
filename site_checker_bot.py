from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import telebot

import os
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttom_check = telebot.types.KeyboardButton('Check the site')
    markup.add(buttom_check)
    bot.send_message(
        message.chat.id,
        'Check the date on the site?',
        reply_markup=markup
    )


def check_table():
    web_driver = webdriver.Chrome()
    web_driver.get('https://tevis.rhein-sieg-kreis.de/?rs')
    elem = web_driver.find_element(
        By.NAME,
        '-Ausländerrechtliche Angelegenheiten-'
    )
    elem.click()
    elem = web_driver.find_element(
        By.NAME,
        'cnc-106'
    )
    elem.send_keys("1")
    elem.send_keys(Keys.RETURN)
    elem = WebDriverWait(web_driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//*[@id="OKButton"]'
        ))
    )
    ActionChains(web_driver).move_to_element(elem).click(elem).perform()
    elem = WebDriverWait(web_driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[@id="ui-id-1"]'
        ))
    )
    if elem is not None:
        cur_title = elem.get_attribute('title')
        elem_title = (f'{cur_title} \n'
                      f'{web_driver.current_url}')
    else:
        elem_title = 'no elements'
    web_driver.quit()
    return elem_title


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Check the site':
        bot.send_message(message.chat.id, check_table())


bot.polling(none_stop=True)
