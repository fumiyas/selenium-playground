#!/usr/bin/env python3
## -*- coding: utf-8 -*- vim:shiftwidth=4:expandtab:

import os
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option('w3c', False) ## for driver.log_types
opts.set_capability('goog:loggingPrefs', { 'browser':'ALL' })
driver = webdriver.Chrome(options=opts)

driver.get('file://' + os.getcwd() + '/chrome-console-log.html')

print(driver.log_types)
for entry in driver.get_log('browser'):
    print(entry)
