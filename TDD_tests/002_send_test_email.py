from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
NM_ML = (By.NAME, "login")
CLCK_PSWD_BTN = (By.XPATH, "//button[@data-testid='enter-password']")
SND_PSWD = (By.XPATH, "//input[@class='password-input svelte-1eyrl7y']")
CLCK_NTR_BTN = (By.XPATH, "//button[@class='second-button svelte-1eyrl7y']")
WRT_LTR = (By.XPATH, "//span[@class='compose-button__txt']")
TO_WHM_FLD = (By.XPATH, "//div[@data-name='to']/div[@data-type='to']//input")
LTTR_FLD = (By.XPATH, "//div[@class='editable-container-jkh5']")
SND_BTN = (By.XPATH, "//span[@class='button2 button2_base button2_primary button2_compact button2_hover-support js-shortcut']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://mail.ru//' )

# 2. Send 'lupusludens' to field 'Имя ящика'
wait.until(EC.presence_of_element_located(NM_ML)).clear()
wait.until(EC.presence_of_element_located(NM_ML)).send_keys('lupusludens')

# 3. CLick on button 'Ввести пароль'
wait.until(EC.presence_of_element_located(CLCK_PSWD_BTN)).click()

# 4. Send 'jzRiA-ap9YJ3' to field 'Пароль'
sleep(4)
wait.until(EC.presence_of_element_located(SND_PSWD)).clear()
wait.until(EC.presence_of_element_located(SND_PSWD)).send_keys('jzRiA-ap9YJ3')

# 5. CLick on button 'Войти'
wait.until(EC.presence_of_element_located(CLCK_NTR_BTN)).click()

# 6. CLick on button 'Написать письмо'
wait.until(EC.presence_of_element_located(WRT_LTR)).click()

# 7. Send 'gurovvic@gmail.com' to field 'Кому'
wait.until(EC.presence_of_element_located(TO_WHM_FLD)).click()
wait.until(EC.presence_of_element_located(TO_WHM_FLD)).clear()
wait.until(EC.presence_of_element_located(TO_WHM_FLD)).send_keys('gurovvic@gmail.com'+ Keys.TAB + Keys.TAB + Keys.TAB + 'Test message')
# driver.switch_to.default_content()

# 8. CLick on button 'Отправить'
wait.until(EC.element_to_be_clickable(SND_BTN)).click()

driver.close()

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()