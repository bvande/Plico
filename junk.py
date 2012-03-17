#!/usr/bin/env python
import nose, core, time
from nose.plugins.attrib import attr

from common.operations import *
from common.homepage import *

from core import get, browserType

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

data = get()
urls = get(r'common\urls.config')
driver = browserType(data['browser'])

login(driver, urls.home, data.user, data.password)
wait = ui.WebDriverWait(driver, 10)
wait.until(driver.find_element_by_id('topRightLinks'))
driver.close()