import os
import time
import pandas as pd
import zipfile
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

ZIP = './downloads/victims.zip'
FILENAME = 'Victims_Age_by_Offense_Category_2022.xlsx'

# Create Chromeoptions instance
options = webdriver.ChromeOptions()


# without nav
options.add_argument("--headless")  # Runs Chrome in headless mode.

# Setting the download path
current_directory = os.getcwd()
download_path = os.path.join(current_directory, "downloads")
if not os.path.exists(download_path):
    os.makedirs(download_path)

prefs = {"download.default_directory": download_path}
options.add_experimental_option("prefs", prefs)
# Adding argument to disable the AutomationControlled flag
options.add_argument("--disable-blink-features=AutomationControlled")

# Exclude the collection of enable-automation switches
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Turn-off userAutomationExtension
options.add_experimental_option("useAutomationExtension", False)

# Setting the driver path and requesting a page
driver = webdriver.Chrome(options=options)

# Changing the property of the navigator value for webdriver to undefined
driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

chrome_service = Service(executable_path=ChromeDriverManager().install())

TIME_TO_WAIT = 10


def espera_elemento_presente(by, value):

    return WebDriverWait(driver, TIME_TO_WAIT).until(
        EC.presence_of_element_located((by, value))
    )


def mark_select(button_id, list_id, option):
    '''This function is used to select an option from a list of options'''
    time.sleep(1)
    espera_elemento_presente(By.ID, button_id).click()

    list_options = espera_elemento_presente(By.ID, list_id).find_element(
        By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'nb-option')
    time.sleep(1)

    [x for x in list_options if str(x.text).strip() == option][0].click()
    time.sleep(1)


def fill_options_nibrs(table_name, year, location):
    '''This function is used to fill the options of the download section'''
    mark_select('dwnnibrs-download-select', 'cdk-overlay-0', table_name)
    mark_select('dwnnibrscol-year-select', 'cdk-overlay-1', year)
    mark_select('dwnnibrsloc-select', 'cdk-overlay-2', location)


try:
    print('Data downloading...')
    driver.get('https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home')

    espera_elemento_presente(
        By.ID, 'home-dwnload-go-btn').click()  # go-download button

    fill_options_nibrs('Victims', '2022', 'Florida')

    espera_elemento_presente(
        By.ID, 'nibrs-download-button').click()  # download button
except:
    print('Error while downloading data, please try again.')

print('Data downloaded with success...')
# DATA FRAME ===========================
time.sleep(5)

archive = zipfile.ZipFile(ZIP, 'r')
xlfile = archive.open(FILENAME)

victims_df = pd.read_excel(xlfile)

victims_df.columns = ['Offense Category', 'Total Victims', '10 and Under', '11-15',
                      '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', '51-55',
                      '56-60', '61-65', '66 and orver', 'Unknown age']

category_index = victims_df.loc[(victims_df['Offense Category'] ==
                                 'Crimes Against Property')].index.values[0]

start_category_index = category_index + 1

categories_df = victims_df.iloc[start_category_index::].drop(
    'Total Victims', axis=1).dropna().reset_index(drop=True)


categories_df.to_csv('./downloads/victims.csv', index=False)

print('\nSrapping and CSV finished with success!!!\n')
