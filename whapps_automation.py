contacts_ ={'234 3988 898':'Jane Doe }

import time
import unittest


not_found = {}
count = 0



nt_fund ={}






deferred = {}
not_found = {}


class WhatsappAndroidTests(unittest.TestCase):


    regpack = """
{} {},
Messgae goes here"""
    reminder_ = """
{} {},
Message goes here"""
    reminder = """
    
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

    def test_text_friend(self):
        #self.whatsapp('know')
        salute = 'Dear'
        name = contacts[phone]
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
            msg_txt.send_keys(self.regpack.format(salute, contacts[phone]))
            send_button = self.driver.find_element_by_id("com.whatsapp.w4b:id/send")
            send_button.click()
            """
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
            send_attached.click()"""
            print('sent', 'count','name:', contacts[phone], 'phone:',phone)
            #count += 1
            #{"x": , "y": }}
            #TouchAction(self.driver).tap(x=292, y=1525).perform()
            #pass
            """search_button = self.driver.find_element_by_id("com.whatsapp:id/menuitem_search")
            search_button.click()
    
            name_search_box = self.driver.find_element_by_id("com.whatsapp:id/search_src_text")
            name_search_box.send_keys('My thoughts')
    
            msg = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("My thoughts")')
            msg.click()
            time.sleep(2)
            text_box = self.driver.find_element_by_id("com.whatsapp:id/entry")
            text_box.send_keys("Hey")
    
            send_button= self.driver.find_element_by_id("com.whatsapp:id/send")
            send_button.click()"""
        except:
            print('count', ': Not found', contacts[phone], phone)
            not_found[phone]= contacts[phone]
    def whatsapp(self, isinstance, *args):
        try:

            from android import activity, mActivity
            from jnius import autoclass, cast
            url = 'https://api.whatsapp.com/send?phone=' + '234{}'.format(isinstance) + "&text=" + 'hello'
            String = autoclass('java.lang.String')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # Environment=autoclass('android.os.Environment')
            intent = Intent()
            self.msg = '{}'.format(msg)
            # uri =Uri.parse("smsto:"+'+2348149402614')
            intent.setAction(Intent.ACTION_VIEW)
            # smsText='hi'

            # intent(Intent.ACTION_SENDTO, uri)
            # intent.setPackage("com.whatsapp")
            # intent.putExtra("sms_body", smsText)
            # intent.putExtra(Intent.EXTRA_SUBJECT, cast('java.lang.CharSequence', String('Fast Perception')))
            # intent.putExtra(Intent.EXTRA_TEXT, cast('java.lang.CharSequence', String('{}'.format(self.msg))))
            # intent.setType('text/plain') #text message

            # global fn_dir
            # self.e =intent.setAction(Intent.ACTION_PICK)
            intent.setData(Uri.parse(url))
            mActivity.startActivityForResult(intent, 0x123)
        except Exception as e:
            print(e)
            #global er
            #er = str(e)
            #Alert()



if __name__ == '__main__':

    #def start():
    #print('clean up',len(contacts_), contacts_)
    print('start with',len(contacts), 'contacts')
    #global phone
    for phone in contacts.keys():
        print('starting')

        #print(phone)

        #suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTests)
        #unittest.TextTestRunner(verbosity=1).run(suite)
        #break
        #print('sent to', contacts[phone], phone)
    print("Didn't find", len(not_found), 'of total:', len(contacts), not_found)
    #start()
    #print(contacts)
    #for item in to_do.keys():
    #    print(to_do[item])
    def remove_invalids():
        remove = recent_rem
        print('Initials', 'contacts:', len(contacts), 'test:',len(remove))
        for val in remove.keys():
            try:
                contacts.pop(val)
            except:
                print("couldn't pop:", val, remove[val])
        print('final result:',len(contacts), contacts)
    #remove_invalids()


