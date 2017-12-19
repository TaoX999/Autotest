#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from appium import webdriver
from time import sleep


class Dance_Repeat_Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android'
        desired_caps['appPackage'] = 'com.iwith.smart'
        desired_caps['appActivity'] = 'com.iwith.smart.iwith_clerk.activity.SplashActivity'
        desired_caps['appWaitActivity'] = 'com.iwith.smart.iwith_control.activity.LanguageSetActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #self.driver.find_element_by_id("com.iwith.smart:id/language_bt_next").click()
        self.driver.find_element_by_xpath("//*[@text='开始点餐']").click()
        sleep(15)

    def tearDown(self):
        # end the session
        pass

    def test_repeat_dance(self):
        
        self.driver.tap([(450,1210),])
        sleep(2)
        self.driver.tap([(520,300),])
        sleep(2)
        x = 0
        while x < 1:
            self.driver.tap([(200,300),])
            sleep(50)
            self.driver.tap([(500,300),])
            sleep(50)
            self.driver.tap([(200,600),])
            sleep(50)
            self.driver.tap([(500,600),])
            sleep(50)
            x += 1
            
        self.assertRaises(None)
        print "test finished"

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Dance_Repeat_Test)
    unittest.TextTestRunner(verbosity=2).run(suite)