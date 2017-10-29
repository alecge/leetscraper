from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


"""
This is an example of using Firefox on windows

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

driver = webdriver.Firefox(firefox_binary = binary)
"""

# Edit this to change the driver used.
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                           desired_capabilities=DesiredCapabilities.CHROME)

def main():
    show_all_elements()

    # Represents problem number as will be listed in file system
    problem = 1

    while True:
        getProblem(problem)
        writeToFile(problem)
        driver.get('https://leetcode.com/problemset/all/')
        driver.implicitly_wait(4)
        problem += 1

def show_all_elements():
    """
    Shows all leetcode problems on a single page by clicking "all" on the dropdown at the bottom
    :return:
    """
    driver.get('https://leetcode.com/problemset/all/')
    driver.implicitly_wait(3)
    show_all_elements = driver.find_element_by_xpath(
        '//*[@id="question-app"]/div/div[2]/div[2]/div[2]/table/tbody[2]/tr/td/span/select')

    for option in show_all_elements.find_elements_by_tag_name('option'):
        if option.text == 'all':
            option.click()
            break


def getProblem(pNumber: int):
    """
    Navigates the browser to the pNumber'th problem.

    :param pNumber: The nth problem (1-indexed) so far.  Premium problems are skipped but do increment pNumber.
    :return:
    """
    print("> Working on problem " + str(pNumber))
    driver.implicitly_wait(2)

    problem_parent = driver.find_element_by_css_selector("""#question-app > div > div:nth-child(2) > div.question-list-base 
                                            > div.table-responsive.question-list-table > table > tbody.reactable-data""")
    problems_raw = problem_parent.find_elements_by_tag_name('tr')

    # Each problem is nested...
    # Get the <td> element containing everything we need
    problemTD = problems_raw[pNumber - 1].find_elements_by_tag_name('td')[2]

    # Get the div containing everything we need from the td element above
    problemDIV = problemTD.find_element_by_tag_name('div')

    # Get the actual element that we can click on
    problem = problemDIV.find_element_by_tag_name('a')
    problem.click()

    print("----> Clicking on problem")

    writeToFile()



def writeToFile(pNumber: int):
    """
    Writes the problem description and solutions in html and plain text to a file under data/

    File naming conventions:
        Problem description:
            p<pNumber>.txt
            e.g. p001.txt, p002.txt, p100.txt

        Solution in HTML:
            s<pNumber>.txt
            e.g. s001.txt, s002.txt, s100.txt

        Solution in plain text:
            s<pNumber>-text.txt
            e.g. s001-text.txt, s002-text.txt, s100-text.txt

    :param pNumber: The nth problem (1-indexed) so far. Premium problems are skipped but do increment pNumber.
    :return: Nothing
    """

    # If this problem is a premium problem, leetcode redirects to a login page
    if "https://leetcode.com/accounts/login/" in driver.current_url:
        driver.back()
        driver.implicitly_wait(3)
        print("----> Premium problem, going back")
    else:

        print("----> Getting description text")

        # Get the element containing the description
        descText = driver.find_element_by_xpath('//*[@id="descriptionContent"]/div[1]/div/div[2]')

        p_file_name = 'data/p' + str(pNumber).zfill(3) + '.txt'

        with open(p_file_name, 'w') as description_file:
            description_file.write(descText.text)


        try:

            print("----> Attempting to get solution")

            # Solutions are in a separate "tab" in the web page, so let's switch to that
            solutionTab = driver.find_element_by_xpath('//*[@id="tab-view-app"]/div/div[1]/nav/a[5]')
            solutionTab.click()

            # Get the actual element containing the solution
            solution = driver.find_element_by_xpath('//*[@id="tab-view-app"]/div/div[2]/div/div[2]/div[1]/div')
            '//*[@id="descriptionContent"]/div[1]/div/div[2]'

            s_file_name = 'data/s' + str(pNumber).zfill(3) + '.txt'
            s_file_name_text = 'data/s' + str(pNumber).zfill(3) + '-text.txt'

            solution_html = solution.get_attribute('innerHTML')

            with open(s_file_name, 'w') as solution_html_file:
                solution_html_file.write(solution_html)

            with open(s_file_name_text, 'w') as solution_text_file:
                solution_text_file.write(solution.text)

        except:
            # No solution if any exception is thrown
            print("----> No solution")

            s_file_name = 'data/s' + str(pNumber).zfill(3) + '.txt'
            s_file_name_text = 'data/s' + str(pNumber).zfill(3) + '-text.txt'

            with open(s_file_name, 'w') as solution_html_file:
                solution_html_file.write("No solution")

            with open(s_file_name_text, 'w') as solution_text_file:
                solution_text_file.write("No solution")
