__author__ = 'Jaime'

from selenium import webdriver
import time
import getpass


def login_facebook(username, password, post):
    url = 'https://www.facebook.com/'

    driver = webdriver.Chrome(executable_path="/home/jaime/Descargas/chromedriver")

    driver.get(url)

    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()
    driver.find_element_by_name('xhpc_message').send_keys(post)
    time.sleep(5)
    buttons = driver.find_elements_by_tag_name('button')
    time.sleep(5)
    for button in buttons:
        if button.text == 'Compartir':
            button.click()


if __name__ == '__main__':
    username = input('Ingrese su usuario: ')
    password = getpass.getpass('\nIngrese su contraseña: ')
    post = input('\nIngrese el texto a publicar: ')
    login_facebook(username, password, post)
