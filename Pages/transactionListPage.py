import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.checkElementPresence import check_element_presence
from selenium.webdriver.support import expected_conditions as EC

class TransactionListPage:
    button_customerLogin_xpath = (By.XPATH, "//button[contains(.,'Customer Login')]")

    startDate_xpath = (By.XPATH, "//input[@id='start']")
    endDate_xpath = (By.XPATH, "//input[@id='end']")

    table_xpath = (By.XPATH, "//table[contains(@class,'table table-bordered table-striped')]")

    def __init__(self, driver):
        self.driver = driver

    def sendStartDate(self, startDateValue):
        wait = WebDriverWait(self.driver, 1)
        # Check for start date element
        if check_element_presence(self.driver, self.startDate_xpath):
            # Click on the Start date
            wait.until(EC.presence_of_element_located(self.startDate_xpath)).click()
            wait.until(EC.presence_of_element_located(self.startDate_xpath)).send_keys(str(startDateValue))
            time.sleep(5)


    def sendEndDate(self, endDateValue):
        wait = WebDriverWait(self.driver, 1)
        # Check for end date element
        if check_element_presence(self.driver, self.endDate_xpath):
            # Click on the End date
            wait.until(EC.presence_of_element_located(self.endDate_xpath)).click()
            wait.until(EC.presence_of_element_located(self.endDate_xpath)).send_keys(str(endDateValue))
            wait.until(EC.presence_of_element_located(self.endDate_xpath)).click()
            time.sleep(5)


    def verifyTransactionIsInTheList(self, amountToDeposit):
        wait = WebDriverWait(self.driver, 1)
        if check_element_presence(self.driver, self.table_xpath):
            # Locate the table (adjust the selector as necessary)
            #table = self.driver.find_element(self.table_xpath)  # Example: By ID
            table = wait.until(EC.presence_of_element_located(self.table_xpath))

            # Get all rows in the table
            rows = table.find_elements(By.TAG_NAME, 'tr')

            # Define the column index you want to check (0 for the first column, 1 for the second, etc.)
            column_index = 1

            # The value you want to check for
            value_to_check = amountToDeposit

            # Initialize a flag to track if the value exists
            value_exists = False

            # Iterate through the rows, skipping the header row if present
            for row in rows[1:]:  # Start from 1 if there's a header row
                # Get the cells in the current row
                cells = row.find_elements(By.TAG_NAME, 'td')

                # Check if the desired column exists in the row
                if len(cells) > column_index:
                    # Extract the value from the specified column
                    cell_value = cells[column_index].text.strip()  # .strip() to remove extra whitespace

                    # Check if the value matches
                    if int(cell_value) == int(value_to_check):
                        value_exists = True
                        break

            # Print the result
            if value_exists:
                print(f'The value "{value_to_check}" exists in the transactions List.')
            else:
                print(f'The value "{value_to_check}" does not exist in the transactions List.')

        time.sleep(2)
