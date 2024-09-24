import time
import pyautogui as pg

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('D:\\Python\\ItemsParser\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://cryptonist.ru")

links = []


def main():
    driver.find_element(By.TAG_NAME, 'html')
    GetLinks()
    WriteLinksInFile()

    time.sleep(5)
    driver.close()
    driver.quit()


def GetLinks():
    time.sleep(5)

    # TODO Аппаратные кошельки и аксессуары
    firms = ['Ledger Nano', 'Cool', "D'CENT", 'Ethereum Card Wallet', 'Tangem', 'Trezor']
    driver.find_element(By.CSS_SELECTOR, '.cd-dropdown-wrapper > .cd-dropdown-trigger').click()
    driver.find_elements(By.CLASS_NAME, 'has-children')[0].click()
    time.sleep(2)
    for i in range(10):
        pg.press('pagedown')
        time.sleep(0.25)
    for firm in firms:
        items = driver.find_elements(By.PARTIAL_LINK_TEXT, firm)
        for item in items:
            try:
                links.append(item.get_attribute('href'))
                print(item.get_attribute('href'))
            except:
                print("Ссылки не найдено!")
    pg.press('home')

    # TODO Хранение резервных копий
    firms = ['Cryptosteel', 'Starter', 'SafePal']
    driver.find_element(By.CSS_SELECTOR, '.cd-dropdown-wrapper > .cd-dropdown-trigger').click()
    driver.find_elements(By.CLASS_NAME, 'has-children')[1].click()
    time.sleep(2)
    for i in range(3):
        pg.press('pagedown')
        time.sleep(0.25)
    for firm in firms:
        items = driver.find_elements(By.PARTIAL_LINK_TEXT, firm)
        for item in items:
            try:
                links.append(item.get_attribute('href'))
                print(item.get_attribute('href'))
            except:
                print("Ссылки не найдено!")
    pg.press('home')

    # TODO U2F токены
    firms = ['Yubikey Bio Type C', 'Yubikey 5C Nano', 'Key']
    driver.find_element(By.CSS_SELECTOR, '.cd-dropdown-wrapper > .cd-dropdown-trigger').click()
    driver.find_elements(By.CLASS_NAME, 'has-children')[5].click()
    pg.press('pagedown')
    pg.press('pagedown')
    time.sleep(2)
    for firm in firms:
        items = driver.find_elements(By.PARTIAL_LINK_TEXT, firm)
        for item in items:
            try:
                links.append(item.get_attribute('href'))
                print(item.get_attribute('href'))
            except:
                print("Ссылки не найдено!")
            if len(links) == 37:
                break
    print(len(links))


def WriteLinksInFile():
    with open('links.txt', 'w') as file:
        for line in range(len(links)):
            file.write(f'{links[line]}\n')


if __name__ == "__main__":
    main()
