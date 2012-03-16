#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getFolders(pdriver):
    return pdriver.find_elements_by_css_selector("a.navLink")
    
def addFolder(pdriver):
    return pdriver.find_element_by_css_selector("a.navAddF")
    
def cabHome(pdriver):
    return pdriver.find_element_by_css_selector(".cabSelPrompt")
    
def cabSelector(pdriver):
    return pdriver.find_element_by_class_name("cabTriDown")
    
def getCabs(pdriver):
    cabSelector(pdriver).click()
    found = pdriver.find_elements_by_css_selector("li.menuIndent") + pdriver.find_elements_by_css_selector("li.menuIndent.menuSelection.showCategoryEntry")
    return filter(lambda x: x.text != "", found)
    
def cabSwitch(pdriver, pcabName):
    for c in getCabs(pdriver):
        if c.text == pcabName:
            c.click()
            return True
    return False