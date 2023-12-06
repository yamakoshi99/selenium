from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # Chromeを自動操作するWebDriverオブジェクトを作成
driver.get("https://www.google.com")  # Googleのページを開く

search_box = driver.find_element_by_name("q")  # 検索ボックスの要素を取得
search_box.send_keys("python")  # 検索ボックスに"Selenium"と入力
search_box.send_keys(Keys.RETURN)  # Enterキーを送信して検索を実行

# 結果ページで何か操作をする場合は、ここでコードを追加します。

# driver.quit()  # ブラウザを閉じて終了
print("Done!")
