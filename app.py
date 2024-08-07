from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import openpyxl
import os
import schedule



class DollarQuote:

    def __init__(self):
        
        self.chrome_options = Options()

        self.arguments = ['--lang=pt-BR', '--window-size=800,800', '--incognito']

        for argument in self.arguments:
            self.chrome_options.add_argument(argument)

        self.chrome_options.add_experimental_option("prefs", {
            'download.directory_upgrade': True,
            'download.prompt_for_download': False,
            "profile.default_content_setting_values.notifications": 2, 
            "profile.default_content_setting_values.automatic_downloads": 1,
        })

        self.driver = webdriver.Chrome(options=self.chrome_options)
    
    
    def get_dollar_quote(self):
        self.driver.get("https://www.google.com/search?q=dolar")
        sleep(5)
        self.cotacao_dolar = self.driver.find_element(By.CLASS_NAME,'DFlfde.SwHCTb').text.replace(',','.')
        return self.cotacao_dolar
        
        
    def save_screenshot(self):
        sleep(2)
        self.date = datetime.now().strftime("%d-%m-%Y-%H-%M")
        self.driver.save_screenshot(f'{self.date}.png')
        sleep(1)
        self.driver.close()
        self.driver.quit()


bot =  DollarQuote()
dollar_quote = bot.get_dollar_quote()
print(dollar_quote)
bot.save_screenshot()
