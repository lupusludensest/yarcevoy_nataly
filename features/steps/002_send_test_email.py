from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()


@then("Send '{lgn}' to field 'Имя ящика'")
def snd_lgn(context, lgn):
    """
    Send 'lupusludens' to field 'Имя ящика'
    """
    context.app.main_page.snd_lgn(lgn)


@then("CLick on button 'Ввести пароль'")
def clck_ntr_pswd_btn(context):
    """
    "CLick on button 'Ввести пароль'"
    """
    context.app.main_page.clck_ntr_pswd_btn()


@step("Send '{pswd}' to field 'Пароль'")
def snd_pswd(context, pswd):
    """
    "Send 'jzRiA-ap9YJ3' to field 'Пароль'"
    """
    context.app.main_page.snd_pswd(pswd)


@then("CLick on button 'Войти'")
def clck_btn_ntr(context):
    """
    "CLick on button 'Войти'"
    """
    context.app.main_page.clck_btn_ntr()


@then("CLick on button 'Написать письмо'")
def clck_btn_wrt_ltr(context):
    """
    CLick on button 'Написать письмо'"
    """
    context.app.main_page.clck_btn_wrt_ltr()


@step("Send 'gurovvic@gmail.com' to field 'Кому'")
def snd_ml_addrss(context):
    """
    "Send 'gurovvic@gmail.com' to field 'Кому'"
    """
    context.app.main_page.snd_ml_addrss()


@then("CLick on button 'Отправить'")
def clck_snd(context):
    """
    "CLick on button 'Отправить'"
    """
    context.app.main_page.clck_snd()