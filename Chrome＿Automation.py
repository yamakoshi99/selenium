from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk

# Chrome WebDriverのオプションを設定
chrome_options = Options()
chrome_options.add_argument("--headless")  # ヘッドレスモードを有効にするオプション

driber = webdriver.Chrome(options=chrome_options, executable_path="./chromedriver")
driber.implicitly_wait(10)
driber.get("https://www.library.chiyoda.tokyo.jp/")

e1 = driber.find_element_by_class_name("schedule-list01__text")
print(e1.text)

