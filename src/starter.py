from selenium import webdriver

driver = webdriver.Chrome(executable_path='../Driver/chromedriver')

driver.get('http://localhost:3000/signin')


