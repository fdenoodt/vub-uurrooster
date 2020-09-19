import datetime
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def navigate_to_schedule_overview():
    driver.get('https://splus.cumulus.vub.ac.be/SWS/v3/evenjr/NL/STUDENTSET/studentset.aspx')

    Type = "Schakel- en Voorbereidingsprogramma's"
    Faculteit = "Wetenschappen en Bio-ingenieurswetenschappen"
    Opleiding = "Computerwetenschappen"
    driver.find_element(By.XPATH, '//td[text()="' + Type + '"]').click()
    driver.find_element(By.XPATH, '//td[text()="' + Faculteit + '"]').click()
    driver.find_element(By.XPATH, '//td[text()="' + Opleiding + '"]').click()


def navigate_to_schedule():
    list_weeks = driver.find_element_by_id('lbWeeks')
    list_weeks_select = Select(list_weeks)
    list_weeks_select.deselect_all()

    query_string = 'Deze week'
    elems = list_weeks.find_elements_by_xpath("//*[contains(text(),'" + query_string + "')]")

    this_week_value = int(elems[0].get_property("value"))
    this_week_value += calculate_amount_weeks_to_add()
    list_weeks.find_element_by_xpath("//option[@value=' " + str(this_week_value) + "']").click()
    driver.find_element_by_id('bGetTimetable').click()


def calculate_amount_weeks_to_add():
    # todo try catch
    weeks_to_add = 0
    # if exactly one argument is given
    if len(sys.argv) == 2:
        weeks_to_add = int(sys.argv[0])

    # add 1 if weekend
    if datetime.datetime.today().weekday() >= 5:
        weeks_to_add += 1
    return weeks_to_add


if __name__ == '__main__':
    driver = webdriver.Edge('msedgedriver.exe')
    navigate_to_schedule_overview()
    navigate_to_schedule()
