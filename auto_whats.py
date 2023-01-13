import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
not_found = {}
count = 0

class WhatsappAndroidTests():
  
    contacts={'234 94590 23 2': 'John Doe'}
    
    regpack = """ Dear {}
    Message goes here

"""

    _regpack_ = """ Dear {}
    Message goes here"""
    reminder = """*
    
{} {},

Message goes here"""
    def setUp(self):
        desired_caps ={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0'  #'9.0'
        desired_caps['deviceName'] = '067902515J105751'  #'DEFFL19801000067'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
        #"appPackage": "com.android.chrome"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()
    def start(self):
        count = 0
        print('starting with contacts of len', len(self.contacts), self.contacts)
        for phone in self.contacts.keys():
            self.test_text_friend(phone)
            count +=1
            print('sent', count)
    def test_text_friend(self, phone):

        desired_caps ={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0'  #'9.0'
        desired_caps['deviceName'] = '067902515J105751'  #'DEFFL19801000067'
        desired_caps['noReset'] = 'true'
        desired_caps['appPackage'] = 'com.android.chrome'
        desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
        #"appPackage": "com.android.chrome"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        #self.whatsapp('know')
        salute = 'Dear'
        name = self.contacts[phone]
        try:
            pw = name.split(' ')
            frst = pw[0] if pw[0] else pw[1]
            if not frst:
                frst = pw[2]
            # print(frst)
            re = frst.split(' ')
            p = ''.join(re)
            # print(p)
            if p == p.upper():
                salute = 'DEAR'
                # print(salute)
            elif p == p.capitalize():
                salute = 'Dear'
                # print(salute)
            else:
                salute = 'Dear'


        except:
            print('Error in salute')
        try:
            search_button = self.driver.find_element_by_id("com.android.chrome:id/url_bar")
            search_button.click()
            if phone[0] =='+':
                pea = phone
            else:
                pea = '+234' + phone
            search_button.send_keys('https://api.whatsapp.com/send?phone=' + '{}'.format(pea) + "&text=" )
            TouchAction(self.driver).tap(x=1011, y=2240).perform()
            time.sleep(.5)
            TouchAction(self.driver).tap(x=525, y=792).perform()
            time.sleep(2)
            msg_win = self.driver.find_element_by_id('com.whatsapp.w4b:id/input_layout_content')
            msg_win.click()
            msg_txt = self.driver.find_element_by_id("com.whatsapp.w4b:id/entry")
            #time.sleep(2)
            msg_txt.send_keys(self.regpack.format(salute, self.contacts[phone]))
            send_button = self.driver.find_element_by_id("com.whatsapp.w4b:id/send")
            send_button.click()
            
            attach_button = self.driver.find_element_by_id("com.whatsapp.w4b:id/input_attach_button")
            attach_button.click()
            time.sleep(1)
            TouchAction(self.driver).tap(x=299, y=1664).perform() #click documents
            time.sleep(1)
            TouchAction(self.driver).tap(x=274, y=299).perform() #click browse
            time.sleep(1)
            TouchAction(self.driver).press(x=193, y=493).move_to(x=423, y=496).release().perform() #long press
            #time.sleep(.1)
            TouchAction(self.driver).tap(x=927, y=591).perform()
            #time.sleep(.1)
            TouchAction(self.driver).tap(x=390, y=1127).perform()
            time.sleep(.1)
            TouchAction(self.driver).tap(x=905, y=150).perform()

            send_attached = self.driver.find_element_by_id("android:id/button1")
            send_attached.click()
            print('sent', 'count','name:', self.contacts[phone], 'phone:',phone)
            print('not found', not_found)
            #count += 1
            #{"x": , "y": }}
            #TouchAction(self.driver).tap(x=292, y=1525).perform()
            #pass
            search_button = self.driver.find_element_by_id("com.whatsapp:id/menuitem_search")
            search_button.click()
    
            name_search_box = self.driver.find_element_by_id("com.whatsapp:id/search_src_text")
            name_search_box.send_keys('My thoughts')
    
            msg = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("My thoughts")')
            msg.click()
            time.sleep(2)
            text_box = self.driver.find_element_by_id("com.whatsapp:id/entry")
            text_box.send_keys("Hey")
    
            send_button= self.driver.find_element_by_id("com.whatsapp:id/send")
            send_button.click()
        except Exception as e:
            print(e, 'count', ': Not found', self.contacts[phone], phone)
            not_found[phone]= self.contacts[phone]
            print('not found', not_found)



if __name__ == '__main__':
    #WhatsappAndroidTests().setUp()
    WhatsappAndroidTests().start()
    pass
new_contact ={}
rt = {}
def re():
    for val in new_contact.keys():
        if ',' in val:
            p = val.split(',')
            for v in p:
                rt[v] = new_contact[val]
        else:
            rt[val] = new_contact[val]
    print(rt)



def rter():
    uy ='grfg'
    er = {}
    def rue():
        for u in uy.keys():
            try:
                if u[0] == '0':
                    er[u[1:]] = uy[u]
                else:
                    er[u] =uy[u]

            except:
                er[u] =uy[u]

        print(er)

def hujs():
    for v in uy.keys():
        try:
            if '+' not in v and '234' in v[:5]:
                er[v.replace('234', '')] = uy[v]
            elif '+234' in v[:5]:
                er[v.replace('+234', '')] = uy[v]
            else:
                er[v] =uy[v]
        except:
            er[v] =uy[v]
    print(er)


contacts=  {}
older = {}
#
def gjiof():
    for old in older.keys():
        try:
            check = contacts[old]
        except:
            print(old, older[old], 'not found')
