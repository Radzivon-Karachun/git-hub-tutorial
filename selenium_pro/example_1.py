from selenium import webdriver
import time


try:
    driver = webdriver.Chrome(executable_path='C:/testFiles/chromedriver.exe')
    driver.get('https://www.googl.com/')
    title = driver.title

    # print('title: ', title)
    assert title == 'Google'

except AssertionError:

    print("Something went wrong!")


finally:
    time.sleep(3)
    driver.close()
    # or
    # driver.quit()
