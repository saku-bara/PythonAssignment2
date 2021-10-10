from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class Parser:
    def __get_page(self, url):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element_by_class_name("huqdoR")).click(driver.find_element(By.CLASS_NAME, 'sc-2nb8qo-0')).perform()
        time.sleep(5)
        return driver.page_source
        
    def __get_info(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        items = soup.find_all('div', class_ = 'svowul-5')
        rows = []
        
        for item in items:
            rows.append(
                {
                    'title':item.find('h3', class_ = 'sc-1q9q90x-0').get_text().strip(),
                    'description': item.find('p', class_ = 'sc-1eb5slv-0').get_text().strip(),
                    'img': item.find('div', class_ = 'gBsDgv').find('img').get('src').strip()
                }
            )
        return rows

    def getting(self, currency):
        url = "https://coinmarketcap.com/currencies/" + currency + "/news/"
        page = self.__get_page(url)
        print(self.__get_info(page))

    

    




