from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()  # Chromeを自動操作するWebDriverオブジェクトを作成
driver.get("https://www.google.com")  # Googleのページを開く

# 検索ボックスの要素を取得して"Selenium"と入力し、検索を実行
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("python")  # ここで検索ボックスに"python"と入力
search_box.send_keys(Keys.RETURN)  # Enterキーを送信して検索を実行

# 検索結果が表示されるまで待機
wait = WebDriverWait(driver, 10)
first_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3")))
# 最初の検索結果をクリック
first_result.click()
<<<<<<< HEAD
=======

>>>>>>> 726ed342f220812439b8002560e3fb15eaec526b
# その他の操作を行うコードをここに追加
# 最後にブラウザを閉じる
# driver.quit()
