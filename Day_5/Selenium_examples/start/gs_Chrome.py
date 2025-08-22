import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--log-level=3")
# options.add_argument("--headless")

service = Service("c:/Courses/BrowserDrivers/chromedriver.exe")

# Variant 1
driver = webdriver.Chrome(options=options)

# Variant 2
# driver = webdriver.Chrome(options=options, service=service)

# Variant 3
# driver = webdriver.Chrome(
#     options=options, 
#     service=Service(ChromeDriverManager().install())
# )
driver.get("http://www.python.org")

assert "Python" in driver.title

element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)

assert "No results found" not in driver.page_source
time.sleep(10)

driver.close()