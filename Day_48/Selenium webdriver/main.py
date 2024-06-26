from selenium import webdriver

chrome_drive_path = "C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

driver = webdriver.Chrome(chrome_drive_path)

driver.get("https://www.amazon.com")
driver.close()
driver.quit()