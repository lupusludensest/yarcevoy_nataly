# Created by rapid at 7/08/2021
Feature: # 002_send_test_email

  Scenario: # 002_send_test_email
    Given Loginpage
    Then Send 'lupusludens' to field 'Имя ящика'
    Then CLick on button 'Ввести пароль'
    And Send 'jzRiA-ap9YJ3' to field 'Пароль'
    Then CLick on button 'Войти'
    Then CLick on button 'Написать письмо'
    And Send 'gurovvic@gmail.com' to field 'Кому'
    Then CLick on button 'Отправить'