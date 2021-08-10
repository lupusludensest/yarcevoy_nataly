from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Screenshot import Screenshot_Clipping
import time

# Locators
URL_FLD = (By.XPATH, "//input[@inputmode='search']")
SRCH_BTN = (By.XPATH, "//button[@class='button search__btn button--color-blue button--v-default button--size-lg']")
SCRT_SCR = (By.XPATH, "(//span[@class='security-level__score'])[2]")
CRTCL_RSK = (By.XPATH, "(//div[@class='severity__count'])[1]")
MDM_RSK = (By.XPATH, "(//div[@class='severity__count'])[2]")
ELVT_RSK = (By.XPATH, "(//div[@class='severity__count'])[3]")
NM_ML = (By.NAME, "login")
CLCK_PSWD_BTN = (By.XPATH, "//button[@data-testid='enter-password']")
SND_PSWD = (By.XPATH, "//input[@class='password-input svelte-1eyrl7y']")
CLCK_NTR_BTN = (By.XPATH, "//button[@class='second-button svelte-1eyrl7y']")
WRT_LTR = (By.XPATH, "//span[@class='compose-button__txt']")
TO_WHM_FLD = (By.XPATH, "//div[@data-name='to']/div[@data-type='to']//input")
LTTR_FLD = (By.XPATH, "//div[@class='editable-container-jkh5']")
SND_BTN = (By.XPATH, "//span[@class='button2 button2_base button2_primary button2_compact button2_hover-support js-shortcut']")


class MainPage(Page):

    # 1 Vulnerability test
    # Login https://spyse.com/
    def lgn_spyse(self, spyse):
        self.driver.get(spyse)

    # Input https://mail.ru/ to search field
    def inpt_our_url(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(URL_FLD)).clear()
        wait.until(EC.presence_of_element_located(URL_FLD)).send_keys(url)

    # Click on Search button
    def clck_srch_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(SRCH_BTN)).click()

    # Find security score, critical risk, medium risk, elevated risk, issuer DN
    def fnd_all_data(self):
        wait = WebDriverWait(self.driver, 10)
        security_score = wait.until(EC.visibility_of_element_located(SCRT_SCR)).text.lower()
        critical_risk = wait.until(EC.visibility_of_element_located(CRTCL_RSK)).text.lower()
        medium_risk = wait.until(EC.visibility_of_element_located(MDM_RSK)).text.lower()
        elevated_risk = wait.until(EC.visibility_of_element_located(ELVT_RSK)).text.lower()
        print(f'Security score: "{security_score}";\nCritical risk: "{critical_risk}";\nMedium risk: "{medium_risk}"\n'
              f'Elevated risk: "{elevated_risk}"')

    # Make a screenshot of the whole page
    def mk_scrnsht(self):
        ob = Screenshot_Clipping.Screenshot()
        url = self.driver.current_url
        today = time.strftime(f'%Y_%m_%d')
        now = time.strftime(f'%H_%M_%S')
        file_name = 'vulnerability_' + today + '_' + now + '.jpg'
        img_url = ob.full_Screenshot(self.driver,
                                     save_path=r'C:\Everything\IT\Testing\Automation_08_09_2019\yarcevoy_nataly\screen_shots', image_name= file_name)
        print(img_url)
    # End of the above code

    # 2 Send 'lupusludens' to field 'Имя ящика'
    def snd_lgn(self, lgn):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(NM_ML)).clear()
        wait.until(EC.presence_of_element_located(NM_ML)).send_keys(lgn)
    # End of the above code

    # 3 CLick on button 'Ввести пароль'
    def clck_ntr_pswd_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(CLCK_PSWD_BTN)).click()
    # End of the above code

    # 4 "Send 'jzRiA-ap9YJ3' to field 'Пароль'"
    def snd_pswd(self, pswd):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(SND_PSWD)).clear()
        wait.until(EC.presence_of_element_located(SND_PSWD)).send_keys(pswd)
    # End of the above code

    # 5 "CLick on button 'Войти'"
    def clck_btn_ntr(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(CLCK_NTR_BTN)).click()
    # End of the above code

    # 6 CLick on button 'Написать письмо'"
    def clck_btn_wrt_ltr(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(WRT_LTR)).click()
    # End of the above code

    # 7 Send 'gurovvic@gmail.com' to field 'Кому'
    def snd_ml_addrss(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(TO_WHM_FLD)).click()
        wait.until(EC.presence_of_element_located(TO_WHM_FLD)).clear()
        wait.until(EC.presence_of_element_located(TO_WHM_FLD)).send_keys(
            'gurovvic@gmail.com' + Keys.TAB + Keys.TAB + Keys.TAB + 'Test message')
    # End of the above code

    # 8 "Click on button 'Отправить'
    def clck_snd(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(SND_BTN)).click()
    # End of the above code









