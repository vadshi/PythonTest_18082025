import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import textract
# для работы с сохраненными файлами
import os
# в именах сохраненных файлов ставится дата
import datetime
# для очистки папки с сохраненными файлами после теста
import shutil
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
import pdfminer
# классы для обработки русского текста в PDF
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


class PriceTestCase(unittest.TestCase):
    savePath = "C:\\Users\\Student\\Downloads\\"
    # подготовка к каждому тесту
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # открытие страницы при начале каждого теста
        self.page = self.driver.get(
            'https://service-online.su/forms/cenniki/'
        )
        # открытие окна авторизации
        elem = self.driver.find_element(By.ID, "enter")
        elem.click()
        time.sleep(3)
        # ввод логина и пароля
        elem = self.driver.find_element(By.NAME, "login")
        elem.send_keys("az0prolyn@heheee.com")
        elem = self.driver.find_element(By.NAME, "password")
        elem.send_keys("242NonUsAuh138w48")
        elem = self.driver.find_element(By.NAME, "soglasie")
        elem.click()
        # нажатие кнопки "Войти"
        elem = self.driver.find_element(By.NAME, "test_enter")
        elem.click()
        # 5 сек ожидания открытия окна
        time.sleep(5)
        # закрытие сообщения об успешном входе
        elem = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label=Close]")
        elem.click()
        time.sleep(2)

    # окончание каждого теста
    def tearDown(self):
        # выход с сайта во избежание блокировки
        # системой защиты от подбора пароля
        ul = self.driver.find_element(By.ID, "menu")
        lis = ul.find_elements(By.TAG_NAME, "li")
        li = lis[-1]
        li.click()
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    # тест на наличие ссылки "Личный кабинет" в меню
    def testAuthorization(self):
        elem = self.driver.find_element(By.ID, "menu")
        self.assertIn("Личный\nкабинет", elem.text)


# тест сохранения одного ценника на английском
    def testOnePrice(self):
        elem = self.driver.find_element(By.ID, "comp_name")
        elem.send_keys("Eurotorg")
        # английский формат даты год/месяц/день
        elem = self.driver.find_element(By.ID, "date")
        elem.clear()
        elem.send_keys("2025/08/20")

        # выбор российского рубля в выпадающем списке валют
        elem = self.driver.find_element(By.NAME, "currency_code")
        elem.click()
        time.sleep(2)
        options = elem.find_elements(By.TAG_NAME, "option")
        for option in options:
            if option.text == "₽ российский рубль":
                option.click()
                break

        elem = self.driver.find_element(By.ID, "tovar_ed_default")
        elem.send_keys("kg")
        elem = self.driver.find_element(By.ID, "tovar_country_default")
        elem.send_keys("RU")

        # таблица с товарами
        elem = self.driver.find_element(By.ID, "tab1")
        tbody = elem.find_element(By.TAG_NAME, "tbody")
        tr = tbody.find_element(By.TAG_NAME, "tr")
        # название товара
        td = tr.find_element(By.CLASS_NAME, "tovar_name")
        field = td.find_element(By.TAG_NAME, "textarea")
        field.send_keys("Candy Southern Night")
        # цена товара - английский формат с точкой
        td = tr.find_element(By.CLASS_NAME, "tovar_cena")
        field = td.find_element(By.TAG_NAME, "input")
        field.send_keys("10.55")

        # жмем ссылку "Скачать"
        elem = self.driver.find_element(By.ID, "download")
        elem.click()
        time.sleep(2)


        # 5 сек ожидания
        # на случай, если Firefox спросит, сохранять файл
        time.sleep(5)

        # проверяем наличие сохраненного файла по названию
        today = datetime.date.today()
        fullpath = (self.savePath + "cenniki_new-" + today.strftime("%Y-%m-%d") + ".pdf")
        self.assertEqual(os.path.isfile(fullpath), True)

        # получаем текст из сохраненного файла
        page = textract.process(fullpath)
        # проверяем наличие введенных значений в тексте файла
        # print(page)
        self.assertIn(b"Eurotorg", page)
        self.assertIn(b"2025/08/20", page)
        self.assertIn(b"kg", page)
        self.assertIn(b"RU", page)
        self.assertIn(b"Candy Southern Night", page)




    # тест сохранения одного ценника на русском
    def testOnePriceRu(self):
        elem = self.driver.find_element(By.ID, "comp_name")
        elem.send_keys("ООО Евроторг")
        elem = self.driver.find_element(By.ID, "date")
        elem.send_keys("20.08.2025")
        # выбор российского рубля в выпадающем списке валют
        elem = self.driver.find_element(By.NAME, "currency_code")
        elem.click()
        options = elem.find_elements(By.TAG_NAME, "option")
        for option in options:
            if option.text == "₽ российский рубль":
                option.click()
                break

        elem = self.driver.find_element(By.ID, "tovar_ed_default")
        elem.send_keys("кг")
        elem = self.driver.find_element(By.ID, "tovar_country_default")
        elem.send_keys("РФ")

        # таблица с товарами
        elem = self.driver.find_element(By.ID, "tab1")
        tbody = elem.find_element(By.TAG_NAME, "tbody")
        tr = tbody.find_element(By.TAG_NAME, "tr")
        # название товара
        td = tr.find_element(By.CLASS_NAME, "tovar_name")
        field = td.find_element(By.TAG_NAME, "textarea")
        field.send_keys("Конфеты Южная ночь")
        # цена товара
        td = tr.find_element(By.CLASS_NAME, "tovar_cena")
        field = td.find_element(By.TAG_NAME, "input")
        field.send_keys("10,55")

        # жмем ссылку "Скачать"
        elem = self.driver.find_element(By.ID, "download")
        elem.click()
        # 5 сек ожидания
        # на случай, если Firefox спросит, сохранять файл
        time.sleep(5)

        # проверяем наличие сохраненного файла по названию
        today = datetime.date.today()
        fullpath = (self.savePath + "cenniki_new-" + today.strftime("%Y-%m-%d") + "-1.pdf")
        self.assertEqual(os.path.isfile(fullpath), True)

        # получаем текст из сохраненного файла
        # открываем файл
        fh = open(fullpath, 'rb')
        # открываем первую страницу
        page_obj = next(PDFPage.get_pages(fh, caching=True, check_extractable=True)) #.__next__()

        resource_manager = PDFResourceManager()
        # создаем объект для вывода текста
        fake_file_handle = io.StringIO()
        # создаем конвертер для извлечения текста из PDF
        converter = TextConverter(resource_manager, fake_file_handle)
        # создаем интерпретатор страницы
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        # извлекаем текст страницы
        page_interpreter.process_page(page_obj)
        # забираем текст страницы в переменную page
        page = fake_file_handle.getvalue()

        # уничтожаем созданные объекты
        converter.close()
        fake_file_handle.close()

        # проверяем наличие введенных значений в тексте файла
        # print(page)
        self.assertIn("ООО Евроторг", page)
        self.assertIn("20.08.2025", page)
        self.assertIn("кг", page)
        self.assertIn("РФ", page)
        self.assertIn("Конфеты Южная ночь", page)
        # цена
        self.assertIn("10", page)
        self.assertIn("55", page)


if __name__ == '__main__':
    unittest.main()
