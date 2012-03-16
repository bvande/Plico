#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def favoriteItems(pdriver):
    return pdriver.find_elements_by_class_name("tr.svItem")
