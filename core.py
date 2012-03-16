#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PilcoTest():
    def __init__(self):
        self.privateData = get()
    
    def setUp(self):
        self.driver = browserType(self.privateData['browser'])

    def tearDown(self):
        self.driver.close()        
        
class get(object):
    def __init__(self, nFile=r'common\private.config'):
        self.v = {}
        
        with open(nFile, 'r') as f:
            for x in f.readlines():
                if x[0] != '#':
                    a = x.split('=')
                    self.v[a[0].strip()] = a[1].strip()
    
    def __getitem__(self, key):
        return self.v.get(key, '')
        
    def __setitem__(self, key, value):
        self.v[key] = value

def browserType(s):
    if s[0].lower() == 'f': return webdriver.Firefox()
    if s[0].lower() == 'i': return webdriver.Ie()
    return webdriver.Ie()
