import csv
import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# TODO фото, цена, категория, мини описание, описание, характеристики
from selenium.webdriver.support.wait import WebDriverWait

s = Service('D:\\Python\\ItemsParser\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

links = []
names = []
prices = []
categories = []
small_info = []
info = []
characteristics = []
photos = []


def main():
    GetLinks()
    GetInfo()
    WriteInCSV()

    time.sleep(5)
    driver.close()
    driver.quit()


def GetLinks():
    with open('links.txt', 'r') as file:
        for line in file:
            links.append(line)
            # if len(links) == 10:
            #     break


def GetInfo():
    for link in links:
        driver.get(link)
        time.sleep(3)
        if links.index(link) == 21:
            pg.moveTo(450, 200)
            pg.leftClick()
        time.sleep(1)
        pg.press('pagedown')

        # TODO Название
        name = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.mb-block-card > h1'))).text
        # name = driver.find_element(By.CSS_SELECTOR, '.mb-block-card > h1').text
        names.append(name)
        # print(name)

        # TODO Цена
        try:
            price = driver.find_element(By.CSS_SELECTOR, ".price > span > span").text
        except:
            price = driver.find_element(By.CSS_SELECTOR, ".price > span").text
        prices.append(price)
        # print(price)

        # TODO Категория
        category = ''
        if links.index(link) <= 21:
            category = "Аппаратные кошельки"
            categories.append(category)
        elif 21 < links.index(link) <= 23:
            category = "Аксессуары"
            categories.append(category)
        elif 23 < links.index(link) <= 29:
            category = "Хранение резервных копий"
            categories.append(category)
        else:
            category = "U2F токены"
            categories.append(category)
        # print(category)

        # TODO Краткое описание
        small_description = driver.find_element(By.CSS_SELECTOR, '.mb-block-card p').text
        small_info.append(f"\"{small_description}\"")
        # print(small_description)

        # TODO Полное описание
        description = driver.find_element(By.CSS_SELECTOR, '#tab-description div').text
        info.append(f"\"{description}\"")
        # print(description)

        # TODO Характеристики
        # time.sleep(0.5)
        # try:
        #     driver.find_element(By.XPATH, '/html/body/section[1]/div/ul[2]/li[2]').click()
        #     time.sleep(1)
        #     columns = driver.find_element(By.XPATH, '/html/body/section[1]/div/div[2]')
        #     titles = columns.find_elements(By.TAG_NAME, 'h3')
        #     values = columns.find_elements(By.TAG_NAME, 'p')
        #     new_values = []
        #     for value in values:
        #         value = value.text
        #         if value != "":
        #             new_values.append(value)
        #     characteristic = ''
        #     for i in range(len(titles)):
        #         characteristic += f'{titles[i].text}: {new_values[i]}, '
        #     characteristics.append(characteristic)
        # except:
        #     try:
        #         driver.find_element(By.XPATH, '/html/body/section[1]/div/div[2]/ul/li[2]').click()
        #         time.sleep(1)
        #         columns = driver.find_element(By.XPATH, '/html/body/section[1]/div/div[2]')
        #         titles = columns.find_elements(By.TAG_NAME, 'h3')
        #         values = columns.find_elements(By.TAG_NAME, 'p')
        #         new_values = []
        #         for value in values:
        #             value = value.text
        #             if value != "":
        #                 new_values.append(value)
        #         characteristic = ''
        #         for i in range(len(titles)):
        #             characteristic += f'{titles[i].text}: {new_values[i]}, '
        #         characteristics.append(characteristic)
        #     except:
        #         print('Характеристик нет!')
        #         characteristics.append('')


        # TODO Фото
        div = driver.find_elements(By.CLASS_NAME, 'row')[1].find_element(By.TAG_NAME, 'div')
        go_to_images = \
        div.find_elements(By.TAG_NAME, 'div')[1].find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'div')[
            1].find_element(By.TAG_NAME, 'div')
        images = go_to_images.find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'img')
        photo = ''
        for image in images:
            image = image.get_attribute('src')
            if image not in photo:
                photo += f'{image}, '
        photos.append(f"\"{photo}\"")


def WriteInCSV():
    with open('items_list.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Товар", "Цена", "Категория", "Краткое описание", "Полное описание", "Характеристики", "Фото"])
        for item in range(len(names)):
            writer.writerow(
                [names[item], prices[item], categories[item], small_info[item], info[item],
                 photos[item]])


if __name__ == "__main__":
    main()
