#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(pdriver, pname, ppassword):
    """
    Takes a browser driver, valid username, and password and will log you into the NetDocuments service.
    """
    try:
        pdriver.get(url.home)
        e = pdriver.find_element_by_id("username")
        e.send_keys(pname)
        e = pdriver.find_element_by_id("password")
        e.send_keys(ppassword)
        pdriver.find_element_by_id("loginBtn").click()
    except:
        return False
    return True

def logout(pdriver):
    """
    Takes a browser driver and will log you out of NetDocuments service.
    """
    try:
        pdriver.get(url.home)
        e = pdriver.find_element_by_link_text("Logout")
        e.click()
    except:
        return False
    return True