from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pendulum
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.ui import Select

months = ['jan', 'feb', 'mrt', 'apr', 'mei', 'jun', 'aug', 'sep', 'okt', 'nov', 'dec']


def translate_numeric_month_to_dutch_full(number):
    return months[number - 1]


def navigate_to_schedule():
    driver = webdriver.Edge('msedgedriver.exe')
    driver.get('https://splus.cumulus.vub.ac.be/SWS/v3/evenjr/NL/STUDENTSET/studentset.aspx')

    driver.find_element_by_id('SCH').click()
    driver.find_element_by_id('WE').click()
    driver.find_element_by_id('SWS_SCH_WE_NL_RS_Computerwet_SET').click()

    today = pendulum.now()
    first_date_of_week = today.start_of('week')
    day = str(first_date_of_week.day)
    month = translate_numeric_month_to_dutch_full(first_date_of_week.month)
    year = str(first_date_of_week.year)

    list_weeks = driver.find_element_by_id('lbWeeks')
    list_weeks_select = Select(list_weeks)
    list_weeks_select.deselect_all()

    query_string = 'Deze week'
    elems = list_weeks.find_elements_by_xpath("//*[contains(text(),'" + query_string + "')]")
    elems[0].click()
    driver.find_element_by_id('bGetTimetable').click()


if __name__ == '__main__':
    navigate_to_schedule()
    while True:
        pass
