#coding:utf-8
import time
import automan.tool.error as error
from selenium.webdriver.common.keys import Keys
from automan.util.tool  import Tool
from selenium.webdriver.common.by import By
import os
import configparser
config = configparser.ConfigParser()
#config.read(os.path.join(os.getcwd() , 'ini') + "zero.conf",encoding="utf-8")
config.read(".\ini\zero.conf",encoding="utf-8")
import os

class zero(object):
    '''
    classdocs
    '''
    def __init__(self):
       '''
       Constructor
       '''
       pass
   
    def zero_username_set(self, browser, value_dict):
        try:
            local_dict = dict(value_dict)
            elem = browser.find_element_by_id(config.get("loginn", "id_sign_u"))
            #elem = browser.find_element_by_id('username')
            elem.send_keys(local_dict["key"])
        except:
            raise error.notfind()
        
        
    def zero_pwd_set(self, browser, value_dict):
        try:
            local_dict = dict(value_dict)
            elem = browser.find_element_by_id('password')
            elem.send_keys(local_dict["key"])
            
        except:
            raise error.notfind()
        
        
        
    def zero_loginbutton_click(self ,browser):
        browser.find_element_by_xpath("//*[@id='global_bk']/ul/li[2]/ul/li[6]/a").click()
        
    def zero_login_click(self ,browser):
        browser.find_element_by_id("submitBtn").click()

    def gmail_usenext_click(self, browser):
        browser.find_element_by_id("identifierNext").click()
        
    def gmail_pass_set(self,browser,value_dict):
        local_dict = dict(value_dict)
        elem = browser.find_element_by_name('password')
        elem.send_keys(local_dict["key"])
        
    def gmail_login_click(self, browser):
        browser.find_element_by_id("passwordNext").click()
        
    def gmail_search_set(self,browser,value_dict):
        local_dict = dict(value_dict)
        elem = browser.find_element_by_name('q')
        elem.send_keys(local_dict["key"])
        elem.send_keys(Keys.RETURN)
    
    def gmail_check_verify(self,browser,value_dict):
        local_dict = dict(value_dict)
        simpleTable = browser.find_element_by_xpath("//table[@class='F cf zt']/tbody" )
        rows = simpleTable.find_elements_by_tag_name("tr")
        #self.assertEquals(3, len(rows))
        result = False
        #Print data from each row
        for row in rows:
            cols = row.find_elements_by_tag_name("td")
            #print row.text
            #line = []2
            line =""
            for col in cols:
                line = line + col.text.encode('utf-8')
            if local_dict["key"] in line:
                print (line)
                result = True
        print (result)       
 
 
