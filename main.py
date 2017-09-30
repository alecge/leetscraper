from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
from time import sleep
import platform
import re


"""
if platform.system() == 'Windows':
    

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

driver = webdriver.Firefox(firefox_binary = binary)
"""

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-beta'
driver = webdriver.Chrome(chrome_options = options)

driver.implicitly_wait(3)

driver.get('https://leetcode.com/problemset/all/')

driver.implicitly_wait(3)
show_all_elements = driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select')

for option in show_all_elements.find_elements_by_tag_name('option'):
    if option.text == 'all':
        option.click()
        break


#problems = driver.find_elements_by_xpath('//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[1]/tr[1]/td[3]/div')

problem_parent = driver.find_element_by_css_selector("""#question-app > div > div:nth-child(2) > div.question-list-base > div.table-responsive.question-list-table > table > tbody.reactable-data""")
problems_raw = problem_parent.find_elements_by_tag_name('tr')
#print(problems)
pNumber = 156

while(True):
    problem_parent = driver.find_element_by_css_selector(
        """#question-app > div > div:nth-child(2) > div.question-list-base > div.table-responsive.question-list-table > table > tbody.reactable-data""")
    problems_raw = problem_parent.find_elements_by_tag_name('tr')

    problem1 = problems_raw[pNumber - 1].find_elements_by_tag_name('td')[2]
    problem2 = problem1.find_element_by_tag_name('div')
    problem = problem2.find_element_by_tag_name('a')

    print(problem)



    problem.click()


    descText = driver.find_element_by_xpath('//*[@id="descriptionContent"]/div[1]/div/div[2]')

    p_file_name = 'data/p' + str(pNumber) + '.txt'

    with open(p_file_name, 'w') as w:
        w.write(descText.text)


    driver.back()
    driver.implicitly_wait(2)
    pNumber += 1




#driver.close()


    """
    solutionTab = driver.find_element_by_xpath('//*[@id="tab-view-app"]/div/div[1]/nav/a[5]')
    solutionTab.click()
    solution = driver.find_element_by_xpath('//*[@id="tab-view-app"]/div/div[2]/div/div[2]/div[1]/div')
    '//*[@id="descriptionContent"]/div[1]/div/div[2]'

    s_file_name = 's' + str(pNumber) + '.txt'

    #strippedSolution = solution.get_attribute('innerHTML')
    #strippedSolution = strippedSolution.replace(u"\u2212", "- ")

    solution_text = solution.get_attribute('innerHTML')

    solution_text = re.sub('<span class="[\w+ \w+]*">', "", solution_text)
    solution_text = re.sub('</span>', '', solution_text)

    #solution_text = solution_text.replace("</span>", "")
    solution_text = solution_text.replace("<em>", "")
    solution_text = solution_text.replace("</em>", "")
    solution_text = solution_text.replace("\\", "")
    print(solution_text)


    with open(s_file_name, 'w') as w:
        w.write(solution_text)
    """