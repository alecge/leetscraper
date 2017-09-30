from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
from time import sleep

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

driver = webdriver.Firefox(firefox_binary = binary)

driver.implicitly_wait(3)

driver.get('https://leetcode.com/problemset/all/')

driver.implicitly_wait(3)

show_all_elements = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select')

print(show_all_elements)

for option in show_all_elements.find_elements_by_tag_name('option'):
    if option.text == 'all':
        option.click()
        break


#problems = driver.find_elements_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[1]/td[3]/div')

problems = driver.find_elements_by_css_selector('#question-app > div > div:nth-child(2) > div.question-list-base > div.table-responsive.question-list-table > table > tbody.reactable-data > tr:nth-child(1) > td:nth-child(3) > div > a')
print(problems)

pNumber = 1

for problem in problems:
    problem.click()
    descText = driver.find_element_by_xpath('//*[@id="descriptionContent"]/div[1]/div/div[2]')
    print(descText.text)

    p_file_name = 'p' + str(pNumber) + '.txt'

    with open(p_file_name, 'w') as w:
        w.write(descText.text)

    solutionTab = driver.find_element_by_xpath('//*[@id="tab-view-app"]/div/div[1]/nav/a[5]')
    solutionTab.click()
    solution = driver.find_element_by_xpath('//*[@id="tab-view-app"]/div/div[2]/div/div[2]/div[1]/div')

    s_file_name = 's' + str(pNumber) + '.txt'

    strippedSolution = solution.get_attribute('innerHTML')
    strippedSolution = strippedSolution.replace(u"\u2212", "- ")

    print(strippedSolution)

    with open(s_file_name, 'a') as w:
        w.write(strippedSolution)

    driver.back()
    sleep(2)
    pNumber += 1




#driver.close()