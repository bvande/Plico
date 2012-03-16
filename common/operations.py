#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

def textOnPage(pdriver, txt, iterations=15):
    try:
        pdriver.find_element_by_xpath('//div[contains(text(), "%s")]'%(txt))
        return True
    except:
        return False

    
def login(pdriver, purl, pname, ppass):
    """
    Takes a browser driver, valid username, and password and will log you into the NetDocuments service.
    """
    try:
        pdriver.get(purl)
        e = pdriver.find_element_by_id("username")
        e.send_keys(pname)
        e = pdriver.find_element_by_id("password")
        e.send_keys(ppass)
        pdriver.find_element_by_id("loginBtn").click()
        WebDriverWait(pdriver, 10).until(pdriver.find_element_by_link_text("Logout"))

    except:
        return False
    return True

def logout(pdriver, purl):
    """
    Takes a browser driver and will log you out of NetDocuments service.
    """
    try:
        pdriver.get(purl)
        e = pdriver.find_element_by_link_text("Logout")
        e.click()
    except:
        return False
    return True
