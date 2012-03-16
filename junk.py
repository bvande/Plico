#!/usr/bin/env python
import nose, core, time
from nose.plugins.attrib import attr

from common.operations import *
from common.homepage import *

from core import get, browserType

data = get()
urls = get(r'common\urls.config')
driver = browserType(data['browser'])

login(driver, urls.home, data.user, data.password)
while True:
    print textOnPage(driver, 'Logged in as')
    time.sleep(1)
    
derp = driver.find_elements_by_tag_name('a')
for x in derp: print x.text

