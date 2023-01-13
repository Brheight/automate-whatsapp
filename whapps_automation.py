contacts_ ={  '8035677488': 'Dr Okechukwu Ekemezie', '8111312517': 'Eluozo Collins', '712187260': 'Dr Kasozi Nathan', '0702916735': 'Dr Kasozi Nathan', '+27123941158': 'Nthabiseng Maude Mthethwa(DBA) Hon.', '+27826351627': 'Nthabiseng Maude Mthethwa(DBA) Hon.', '02089613888': 'Iliyasu Maisanda', '07939007787': 'Iliyasu Maisanda', '8062611560': 'Oloruntoba Bamidele', '+233200429430': 'Igiri Kenneth Chidi', '+233544904920': 'Igiri Kenneth Chidi', '8033358591': 'Engr.Haladu Mohammad Zarada', '8032739251': 'Dr.Maurice Nwabueze Obasi', '8128678873': 'Aniefiok Thomas', '+66618391428': 'Mohammed Saeed Suleiman', '7088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8023705659': 'Misso Francis', '8173078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '8055266838': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '904530629': 'Abayomi Bello', '8034071116': 'Paul Nnamah ', '+61[0]755808331': 'Assoc. Prof.Chris O.Ifediora', '+61[0]458183994': 'Assoc. Prof.Chris O.Ifediora', '8033107505': 'Mrs Juliet Ogedi David - west', '8064657799': 'Dr Joseph Rankin', '8102875997': 'Dr Joseph Rankin', '8071827748': 'Idornigie Ide Christopher', '+234 (1) 2713990': 'Kayode Akintolu', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB','7046852104': 'Nkem Joseph-Palmer', '8103756894': 'Reginald Udenze Ihedike', '7068600006': 'Kennedy Akpan', '9027936331': 'Kennedy Akpan', '8056038074': 'Onabekun Isiaka Adekunle', '722599621': 'Peter Okeyo Oraro'}

import time
import unittest

test =  {'8140122664':'BENARD ADEWOLE,', '706 6282414':'Bright Adewole', '8059890169':'Patience'}
#FILLED  FORM '+23279881111':'Dipo Gbenro''+23276368359':'Dipo Gbenro'
#responded '8033377261':'Prof. Basil O.Nwosu'
#blacklist  '8099577770': 'Kevin B.Eluemunor','8077757557': 'Kevin B.Eluemunor',
#deferred #234 - 8188688366 Ujunwa Rosemary Felicia(Mrs), '8032437263': 'ALADE, Ibiwumi A.Ph.D','9098109072':'Stephen Bamidele Ogodo',
#215-329-4154, Claudia Gale
not_found = {}
count = 0
to_do = {'plaques':'none', 'certificates':'enough', 'A4 paper':'half rim', 'conference papers':'none', 'stapler':'',
        'seal':'unchecked','punches pockets':'unchecked','send letter to dsp amida':'', 'ID card':'tickets',
'send reminders to paid participants':'undone', 'malt drinks':'none', 'cashew packs':'none',
         'folders':'26', 'stickers':'50', 'agenda':'unchecked'}


#DISTANCE LEARNING
nt_fund ={}
#dec responded '8037362923': 'Akubueze Chibuzo H.',


#'7020677189': 'Ndubuwa Ugwunna Victor', '7035558287': 'Stephen Eche', '9058546775': 'Kelechi li','8069317779': 'Titi Yakubu', '7046383713': 'Sina Sofola, SAN', '7046216417': 'Sina Sofola, SAN',  '8037262350': 'George Idiaghe','7020677189': 'Ndubuwa Ugwunna Victor',  '7035558287': 'Stephen Eche', '9058546775': 'Kelechi li', '8035677488': 'Dr Okechukwu Ekemezie', '8111312517': 'Eluozo Collins', '712187260': 'Dr Kasozi Nathan', '0702916735': 'Dr Kasozi Nathan', '+27123941158': 'Nthabiseng Maude Mthethwa(DBA) Hon.', '02089613888': 'Iliyasu Maisanda', '07939007787': 'Iliyasu Maisanda', '8062611560': 'Oloruntoba Bamidele', '+233544904920': 'Igiri Kenneth Chidi', '8033358591': 'Engr.Haladu Mohammad Zarada', '8128678873': 'Aniefiok Thomas', '+66618391428': 'Mohammed Saeed Suleiman', '7088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara','8173078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '8055266838': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '904530629': 'Abayomi Bello', '8034071116': 'Paul Nnamah ', '+61[0]755808331': 'Assoc. Prof.Chris O.Ifediora', '8033107505': 'Mrs Juliet Ogedi David - west', '8064657799': 'Dr Joseph Rankin', '8102875997': 'Dr Joseph Rankin', '+234 (1) 2713990': 'Kayode Akintolu', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB',   '7046852104': 'Nkem Joseph-Palmer', '8103756894': 'Reginald Udenze Ihedike', '9027936331': 'Kennedy Akpan', '8056038074': 'Onabekun Isiaka Adekunle', '722599621': 'Peter Okeyo Oraro'}
#sent to sent to Igenegbai Christiana Joy 8033118894

#november already responded '8172925952': 'Seun Sodipe', '8029147144': 'Pam Dung Kim','8033341416': 'OLANIRAN ADERIBIGBE','8069766002': 'Ahmad Yahuza Getso', '9036683244': 'Musari Mathew', '8060895366': 'Musari Mathew','8035881242': 'Emmanuel Akissa', '7011990709': 'Ogunbiyi - Davies Biodun Abiola','8033886655': 'Seun Sodipe',
#dec respon  '8023705659': 'Misso Francis',
#deferred  '94615700': 'Aminu A.Sadiq','8023935869': 'Aminu A.Sadiq',

remove = {'7020677189': 'Ndubuwa Ugwunna Victor', '7035558287': 'Stephen Eche', '9058546775': 'Kelechi li',
          '02089613888': 'Iliyasu Maisanda', '07939007787': 'Iliyasu Maisanda', '8062611560': 'Oloruntoba Bamidele',
          '+233544904920': 'Igiri Kenneth Chidi', '8033358591': 'Engr.Haladu Mohammad Zarada', '8037362923': 'Akubueze Chibuzo H.',
          '8055076706': 'Olajide Solomon Ojo', '8128678873': 'Aniefiok Thomas', '+66618391428': 'Mohammed Saeed Suleiman',
          '8033335091': 'Barr. Miss Chigozie Ifeoma Nwagbara', '7088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara',
          '8156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8037109285': 'Ndifreke Andrew - Essien', '8023705659': 'Misso Francis',
          '8077399795': 'Misso Francis', '8033078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '8173078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB',
          '8055266838': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '904530629': 'Abayomi Bello', '+61[0]755808331': 'Assoc. Prof.Chris O.Ifediora',
          '8033467900': 'Dr.Chukwunonso Izuchukwu Pharm.D, CMC, FIMC', '8033107505': 'Mrs Juliet Ogedi David - west', '8064657799': 'Dr Joseph Rankin',
          '8102875997': 'Dr Joseph Rankin', '7037905644': 'Idornigie Ide Christopher', '+234 (1) 2713990': 'Kayode Akintolu',
          '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB','7046852104': 'Nkem Joseph-Palmer', '8103756894': 'Reginald Udenze Ihedike', '9027936331': 'Kennedy Akpan',
          '8056038074': 'Onabekun Isiaka Adekunle', '722599621': 'Peter Okeyo Oraro', '8098929477': 'Dr. Olotu, O. Ayopo', '8033126206': 'Chuka Unachukwu',
           '706334788': 'DSP Amida S.A', '8029065676': 'DSP Amida S.A', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke',
          '8080767155': 'Chukwudi Iwuozor', '8033262326': 'Ezeogbuefi Gabriel .O', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8054055960': 'Tosin Adelowo',
          '7020677189':'Ndubuwa Ugwunna Victor','8038642614':	'Jayeoba, Moses A','7035558287'	:'Stephen Eche', '9058546775'	:'Kelechi li',
          '8172925952': 'Seun Sodipe','8037262350': 'George Idiaghe','8033047278': 'Nasamu Ibrahim','8035677488': 'Dr Okechukwu Ekemezie',
          '8111312517': 'Eluozo Collins', '712187260': 'Dr Kasozi Nathan','0702916735': 'Dr Kasozi Nathan','+27123941158': 'Nthabiseng Maude Mthethwa(DBA) Hon.',
          '9029461146' :'Oyinloye Oyedele P','8034932689':'Beeson Lawson', '7012121234':'Chuka Unachukwu','8035136609':'Stephen Bamidele Ogodo',
          '8056659371':'Dr. Olotu, O. Ayopo' , '7035466027': 'Dr.Emmanuel Oladipo Akogun', '8069317779': 'Titi Yakubu', '7046383713': 'Sina Sofola, SAN',
 '7046216417': 'Sina Sofola, SAN',
'8173015230':'AKINLAMILO, ELLIOT OLAFISOYE',}

deferred = {}
#nov deferred'94615700': 'Aminu A.Sadiq', '8023935869': 'Aminu A.Sadiq',


#paid '8070321322': 'Okorie, John N.',
#'7062883006': 'Debby Oluyinka Daramola', '9097778162': 'Debby Oluyinka Daramola',
#recent_rem = {'8037035028': 'Prof. John Y. Dung-gwom', '+256417201019': 'Adekemi Ndieli',  '8167353993': 'Mr. Tope Oluwadare', '+16464345929': 'IDOGHO EMMANUEL', '8037126431': 'Akachukwu Moses Chukwudi', '8189624547': 'Benson Ndaji', '8064710849': ' Benson Ndaji', '+447741368789': 'Salisu Uba'}
#already responded  '8039098931': 'JAMES SONDE',  '8036342106': 'KASSIM IDRIS' ,
#remove '8069128653': 'Dr Arome Salifu',
#sent  '8055427409': 'Prof. I.a. Onimawo',


#dec campaign

#already responded '7030834395': 'Engr. Mahraz Karaye','8060740202':'Dr Musa Liman',
#sent
#
#
#
#'8022449020': 'Akubueze Chibuzo H.',
#wrong name '8144513831': 'Comrade DR Mk Adam Rano (Dr Muhammad Kabir Adam)',
#dec responded
not_found = {}

#'8173245448': 'Shirley Ehru Nehemiah',
class WhatsappAndroidTests(unittest.TestCase):


    regpack = """*Gentle Reminder: Certification for Chartered Management Status Holds As Planned*
{} {},

Please, be reminded that the scheduled Certification/Induction for Chartered Management Status will hold as planned in Lagos, Nigeria as follows::

Lagos:

Date: *Thursday, 16th December, 2021.*

Time: *11.00am prompt.*

Venue: *Lagos Chamber of Commerce and Industry (LCCI) Conference and Exhibition Centre,*

Plot 10, Nurudeen Olowopopo Street, Behind MKO, Abiola Garden, Alausa, Lagos.

Please Note: There would be *no Abuja session* this time instead we have made arrangements for those who may not make it to *participate virtually*. Please notify us if you would be participating physically or virtually.


There is provision for you to make payment and, or to complete your registration at the venue, in case you have not done yours.

We are available to respond to further inquiries.

We shall be expecting you.
Many thanks and best regards.

*Michael Adewole Okara*, (ChMC, FIMC, CMC, arpa)
Board Representative.
+2348035796502 | mcscglobal.org"""
    reminder_ = """*Gentle Reminder: Certification for Chartered Management Status Holds As Planned*
{} {},

Please, be reminded that the scheduled Certification/Induction for Chartered Management Status will hold as planned in Abuja, Nigeria as follows:

Abuja:
*Date:* Wednesday, 13th October, 2021.
*Time:* 11.00am prompt.
*Venue:* Silk Road Restaurant, Sinoki House,
5th Floor, Plot 770, Off Samuel Ademulegun Avenue, Opp. Federal Ministry of Transport, CBD, Abuja-FCT.

There is provision for you to make payment and, or to complete your registration at the venue, in case you have not done yours.

We are available to respond to further inquiries.

We shall be expecting you tomorrow.
Many thanks and best regards.

Michael Adewole Okara, (ChMC, FIMC, CMC, arpa)
Board Representative.
+2348035796502 | mcscglobal.org"""
    reminder = """*Gentle Reminder: December Event*
    
{} {},

Thank you for your interest in our certification. It gives us great joy to inform you that our next event has been scheduled for the month of December to hold on the 16th in Lagos. 
There would be no Abuja session this time instead we have made arrangements for those who may not make it to participate virtually. 
We hope you would be better disposed this time. We shall immediately follow up this mail with your invite.

Many thanks and best regards.

Michael Adewole Okara, (ChMC, FIMC, CMC, arpa)
Board Representative.
+2348035796502 | mcscglobal.org"""
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



#start new

import time
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

test =  {'8140122664':'BENARD ADEWOLE,', '706 6282414':'Bright Adewole', '8059890169':'Patience'}
#FILLED  FORM '+23279881111':'Dipo Gbenro''+23276368359':'Dipo Gbenro'
#responded '8033377261':'Prof. Basil O.Nwosu'
#blacklist  '8099577770': 'Kevin B.Eluemunor','8077757557': 'Kevin B.Eluemunor',
#deferred #234 - 8188688366 Ujunwa Rosemary Felicia(Mrs), '8032437263': 'ALADE, Ibiwumi A.Ph.D','9098109072':'Stephen Bamidele Ogodo', '8060740202':'Dr Musa Liman'
#215-329-4154, Claudia Gale
not_found = {}
count = 0
to_do = {'plaques':'none', 'certificates':'enough', 'A4 paper':'half rim', 'conference papers':'none', 'stapler':'',
         'seal':'unchecked','punches pockets':'unchecked','send letter to dsp amida':'', 'ID card':'tickets',
         'send reminders to paid participants':'undone', 'malt drinks':'none', 'cashew packs':'none',
         'folders':'26', 'stickers':'50', 'agenda':'unchecked'}

_contacts_ ={  '8035677488': 'Dr Okechukwu Ekemezie', '8111312517': 'Eluozo Collins', '712187260': 'Dr Kasozi Nathan', '0702916735': 'Dr Kasozi Nathan', '+27123941158': 'Nthabiseng Maude Mthethwa(DBA) Hon.', '+27826351627': 'Nthabiseng Maude Mthethwa(DBA) Hon.', '02089613888': 'Iliyasu Maisanda', '07939007787': 'Iliyasu Maisanda', '8062611560': 'Oloruntoba Bamidele', '+233200429430': 'Igiri Kenneth Chidi', '+233544904920': 'Igiri Kenneth Chidi', '8033358591': 'Engr.Haladu Mohammad Zarada', '8037362923': 'Akubueze Chibuzo H.', '8032739251': 'Dr.Maurice Nwabueze Obasi', '8128678873': 'Aniefiok Thomas', '+66618391428': 'Mohammed Saeed Suleiman', '7088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8023705659': 'Misso Francis', '8173078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '8055266838': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '904530629': 'Abayomi Bello', '8034071116': 'Paul Nnamah ', '+61[0]755808331': 'Assoc. Prof.Chris O.Ifediora', '+61[0]458183994': 'Assoc. Prof.Chris O.Ifediora', '8033107505': 'Mrs Juliet Ogedi David - west', '8064657799': 'Dr Joseph Rankin', '8102875997': 'Dr Joseph Rankin', '8071827748': 'Idornigie Ide Christopher', '+234 (1) 2713990': 'Kayode Akintolu', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7046852104': 'Nkem Joseph-Palmer', '8103756894': 'Reginald Udenze Ihedike', '7068600006': 'Kennedy Akpan', '9027936331': 'Kennedy Akpan', '8056038074': 'Onabekun Isiaka Adekunle', '722599621': 'Peter Okeyo Oraro'}
#DISTANCE LEARNING  '7011990709': 'Ogunbiyi - Davies Biodun Abiola',
nt_fund ={}
#'7020677189': 'Ndubuwa Ugwunna Victor', '7035558287': 'Stephen Eche', '9058546775': 'Kelechi li', '94615700': 'Aminu A.Sadiq','8069317779': 'Titi Yakubu', '7046383713': 'Sina Sofola, SAN', '7046216417': 'Sina Sofola, SAN', '8023935869': 'Aminu A.Sadiq', '8172925952': 'Seun Sodipe',  '8037262350': 'George Idiaghe','7020677189': 'Ndubuwa Ugwunna Victor',  '7035558287': 'Stephen Eche', '9058546775': 'Kelechi li', '8035677488': 'Dr Okechukwu Ekemezie', '8111312517': 'Eluozo Collins', '712187260': 'Dr Kasozi Nathan', '0702916735': 'Dr Kasozi Nathan', '+27123941158': 'Nthabiseng Maude Mthethwa(DBA) Hon.', '02089613888': 'Iliyasu Maisanda', '07939007787': 'Iliyasu Maisanda', '8062611560': 'Oloruntoba Bamidele', '+233544904920': 'Igiri Kenneth Chidi', '8033358591': 'Engr.Haladu Mohammad Zarada', '8037362923': 'Akubueze Chibuzo H.', '8128678873': 'Aniefiok Thomas', '+66618391428': 'Mohammed Saeed Suleiman', '7088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8023705659': 'Misso Francis', '8173078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '8055266838': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '904530629': 'Abayomi Bello', '8034071116': 'Paul Nnamah ', '+61[0]755808331': 'Assoc. Prof.Chris O.Ifediora', '8033107505': 'Mrs Juliet Ogedi David - west', '8064657799': 'Dr Joseph Rankin', '8102875997': 'Dr Joseph Rankin', '+234 (1) 2713990': 'Kayode Akintolu', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7046852104': 'Nkem Joseph-Palmer', '8103756894': 'Reginald Udenze Ihedike', '9027936331': 'Kennedy Akpan', '8056038074': 'Onabekun Isiaka Adekunle', '722599621': 'Peter Okeyo Oraro'}
#sent to sent to Igenegbai Christiana Joy 8033118894





remove = {'7020677189': 'Ndubuwa Ugwunna Victor', '8038642614': 'Jayeoba, Moses A', '7035558287': 'Stephen Eche', '9058546775': 'Kelechi li',
          '02089613888': 'Iliyasu Maisanda', '07939007787': 'Iliyasu Maisanda', '8062611560': 'Oloruntoba Bamidele',
          '+233544904920': 'Igiri Kenneth Chidi', '8033358591': 'Engr.Haladu Mohammad Zarada', '8037362923': 'Akubueze Chibuzo H.',
          '8055076706': 'Olajide Solomon Ojo', '8128678873': 'Aniefiok Thomas', '+66618391428': 'Mohammed Saeed Suleiman',
          '8033335091': 'Barr. Miss Chigozie Ifeoma Nwagbara', '7088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara',
          '8156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8037109285': 'Ndifreke Andrew - Essien', '8023705659': 'Misso Francis',
          '8077399795': 'Misso Francis', '8033078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '8173078252': 'PETER OMOKARO MBA, FIMC, CMC, FCIB',
          '8055266838': 'PETER OMOKARO MBA, FIMC, CMC, FCIB', '904530629': 'Abayomi Bello', '+61[0]755808331': 'Assoc. Prof.Chris O.Ifediora',
          '8033467900': 'Dr.Chukwunonso Izuchukwu Pharm.D, CMC, FIMC', '8033107505': 'Mrs Juliet Ogedi David - west', '8064657799': 'Dr Joseph Rankin',
          '8102875997': 'Dr Joseph Rankin', '7037905644': 'Idornigie Ide Christopher', '+234 (1) 2713990': 'Kayode Akintolu',
          '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7046852104': 'Nkem Joseph-Palmer', '8103756894': 'Reginald Udenze Ihedike', '9027936331': 'Kennedy Akpan',
          '8056038074': 'Onabekun Isiaka Adekunle', '722599621': 'Peter Okeyo Oraro', '8098929477': 'Dr. Olotu, O. Ayopo', '8033126206': 'Chuka Unachukwu',
          '7030834395': 'Engr. Mahraz Karaye', '706334788': 'DSP Amida S.A', '8029065676': 'DSP Amida S.A', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke',
          '8080767155': 'Chukwudi Iwuozor', '8033262326': 'Ezeogbuefi Gabriel .O', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8054055960': 'Tosin Adelowo',
          '7020677189':'Ndubuwa Ugwunna Victor','8038642614':	'Jayeoba, Moses A','7035558287'	:'Stephen Eche', '9058546775'	:'Kelechi li',
          '8172925952': 'Seun Sodipe','8037262350': 'George Idiaghe','8033047278': 'Nasamu Ibrahim','8035677488': 'Dr Okechukwu Ekemezie',
          '8111312517': 'Eluozo Collins', '712187260': 'Dr Kasozi Nathan','0702916735': 'Dr Kasozi Nathan','+27123941158': 'Nthabiseng Maude Mthethwa(DBA) Hon.',
          '9029461146' :'Oyinloye Oyedele P','8034932689':'Beeson Lawson', '7012121234':'Chuka Unachukwu','8035136609':'Stephen Bamidele Ogodo',
          '8056659371':'Dr. Olotu, O. Ayopo' , '7035466027': 'Dr.Emmanuel Oladipo Akogun', '8069317779': 'Titi Yakubu', '7046383713': 'Sina Sofola, SAN',
          '7046216417': 'Sina Sofola, SAN', '94615700': 'Aminu A.Sadiq', '8023935869': 'Aminu A.Sadiq',
          '8173015230':'AKINLAMILO, ELLIOT OLAFISOYE','8113337777':' Dr Arome Salifu',}

deferred = {'8033886655': 'Seun Sodipe', '8070341328': 'Engr. Okurerie Ajiroghene Ogedegbe FNSE', '7037905644': 'Idornigie Ide Christopher',  '+233200429430': 'Igiri Kenneth Chidi','+233544904920': 'Igiri Kenneth Chidi','8094773839': 'Francois Hounda DOSSOU','7062883006': 'Debby Oluyinka Daramola', '9097778162': 'Debby Oluyinka Daramola',  '8032327228': 'Prof Samuel Ogunwale Ogundiran', '8030917088': 'Prof Samuel Ogunwale Ogundiran',
            '7030834395': 'Engr. Mahraz Karaye','8071827748': 'Idornigie Ide Christopher', }
#recent_rem = {'8037035028': 'Prof. John Y. Dung-gwom', '+256417201019': 'Adekemi Ndieli', '8070321322': 'Okorie, John N.', '8167353993': 'Mr. Tope Oluwadare', '+16464345929': 'IDOGHO EMMANUEL', '8037126431': 'Akachukwu Moses Chukwudi', '8189624547': 'Benson Ndaji', '8064710849': ' Benson Ndaji', '+447741368789': 'Salisu Uba'}
#already responded  '8039098931': 'JAMES SONDE',  '8036342106': 'KASSIM IDRIS' ,'8034515945': 'Victor O. Ihebinike',
#remove '8069128653': 'Dr Arome Salifu',
#sent  '8055427409': 'Prof. I.a. Onimawo',
contacts__= {'8035446978': 'Promise Nwafor A Anelechi', '+256771003594': ' Adekemi Ndieli','8023361732': 'Prof. Kessington Obahiagbon', '8052362288': 'Moses Mogbolu', '8159552222': ' Moses Mogbolu', '8064499724': 'Mr. S. Kola Adekoya', '8055776655': 'Pat Amaje', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO','8034240632': 'Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc', '8072599298': ' Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc','9097512017': 'Dr.Ashikia Festus Uwakhemen', '8033509752': 'Idumonza Isidahomhen', '8030717044': 'Derek Omoleh', '8033118894': 'Igenegbai Christiana Joy', '8034373712': 'Ugwuoke Emeka Emmanuel', '8033518361': 'Ikechukwu Oliobi', '9028888903': 'Ikechukwu Oliobi', '8034551482': 'George Chinonso - Obi', '7067941550': 'Bldr.Alvary A.Durkwa', '8023245490': 'Debbie Akwara', '8067742773': 'Mr.Awusa Peter Ewa', '8035693740': 'Prince Bola Olusegun Aina', '8034315211': 'Olatunde Sowunmi', '9039231107': 'Joshua Samuel', '8061572906': 'Uwem Mkpong Archibong', '7080858791': 'Uchenna Ohaeri PMP', '8036197738': 'Aromeh Sunday Adole', '8027291738': 'Christwealth Kolawole', '8037829881': 'Maharaz Saad', '8069680993': 'Orkuma Anyoko - Shaba', '8039689404': 'Wilson Obidah, PhD', '8035672752': 'Victoria', '9036683244': 'Musari Mathew', '8060895366': 'Musari Mathew', '8032825342': 'Engr.Olatunde Michael Ibrahim', '8188541950': 'Engr.Olatunde Michael Ibrahim', '8051500690': 'Osinuga Rahman', '8062411073': 'Bala, Sunday', '8066789611': 'Leonard Nzenwa', '8032195105': 'Dr.Victor Evans.', '8058434421': 'Jatto Osabuhen Jonathan', '8056488800': 'Akinbebije Damilola', '8033597679': 'Mr. Adigun Oluwamayowa Oluwaseun Kingsley', '8035881242': 'Emmanuel Akissa', '8029147144': 'Pam Dung Kim', '8023152210': 'Oke Olabamiji', '8036206061': ' Oke Olabamiji', '8033015230': ' AKINLAMILO, ELLIOT OLAFISOYE', '8069766002': 'Ahmad Yahuza Getso',  '8072661313': 'Alaghala, Alphons L', '8037257819': 'OSUJI ALBERTO OBINNA', '8035983539': 'Shitery Aaron Istifanus', '8035691309': 'Olusegun Adepoju', '8033496839': 'Dr. Charles Anosike FCMI, MNIM GPM', '8032007440': 'Mr.Erere Oyibo - Rhokaye', '8032479757': 'Aiyedun Olubunm FCIS, MTM', '8022449020': 'Akubueze Chibuzo H.', '8030618326': 'D.Tola Winjobi, PhD', '8082008222': 'D.Tola Winjobi, PhD', '8036469928': 'Mohammed Saeed Suleiman', '8068056242': 'Markus Njidda Uba', '8055928327': 'Rev. Sr. Paulette Ekejiuba, PhD', '8144513831': 'Comrade DR Mk Adam Rano (Dr Muhammad Kabir Adam)', '8086633083': 'Kayode Akintolu', '8037093585': 'Nkem Joseph-Palmer', '9023924412': 'Nkem Joseph-Palmer', '8023204138': 'Elvis Onuora FCA, FCTI', '8052913643': 'Abimbola Omolabi PhD', '8033172828': 'Abimbola Omolabi PhD', '8052448149': 'JOSEPH HUMPHREY KABE', '7039554117': 'Job Ayodele Ekundayo', '8033865790': 'Prof. Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart', '8036005365': 'Muhammad Kachallah', '8034106448': 'Lizzy Igbine Mrs.', '8033778222': 'Frederick Bethel Saduwa', '8033341079': 'ISERE Joseph', '8173245448': 'Shirley Ehru Nehemiah', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '7084415597': 'Ismaila Haliru Zarma', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', '7036481502': 'Eni Okoi, Esq.', '8149575705': 'Sylvester Ejiofor', '8032601105': 'Hon. Anselm C. Onuorah', '7069551267': 'Beeson Lawson', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '8037875416': 'Adeniyi Aturamu MNIOB ', '8098449890': 'Adeniyi Aturamu MNIOB ', '7032220542': 'PIUS IPUOLE', '8033341416': 'OLANIRAN ADERIBIGBE', '8036754537': 'Ogechukwu Eucharia Maduka', '8062862692': 'Victor Bisong', '8037879235': 'Zuhair Jibril', '7060772784': 'Victor Obioma Uche', '8033344595': 'Oladejobi Godwin Adebola', '8033156025': 'Engr Aishatu Aliyu Umar, FNSE', '8095000000': 'Engr Aishatu Aliyu Umar, FNSE', '8163686103': 'Dr. Ola Adigun-daniels', '8061296216': 'Godwin Okoko', '8030824948': 'Ogunmefun Toyin', '8131538812': 'SP Onyejegbu Basilia Cynthia', '7088607443': 'Prince Amaefula', '8037012676': 'Oyinloye Oyedele P.'}



not_found = {}
contacts= {'8035446978': 'Promise Nwafor A Anelechi', '+256771003594': ' Adekemi Ndieli','8023361732': 'Prof. Kessington Obahiagbon', '8052362288': 'Moses Mogbolu', '8159552222': ' Moses Mogbolu', '8064499724': 'Mr. S. Kola Adekoya', '8055776655': 'Pat Amaje', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO','8034240632': 'Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc', '8072599298': ' Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc','9097512017': 'Dr.Ashikia Festus Uwakhemen', '8033509752': 'Idumonza Isidahomhen', '8030717044': 'Derek Omoleh', '8033118894': 'Igenegbai Christiana Joy', '8034373712': 'Ugwuoke Emeka Emmanuel', '8033518361': 'Ikechukwu Oliobi', '9028888903': 'Ikechukwu Oliobi', '8034551482': 'George Chinonso - Obi', '7067941550': 'Bldr.Alvary A.Durkwa', '8023245490': 'Debbie Akwara', '8067742773': 'Mr.Awusa Peter Ewa', '8035693740': 'Prince Bola Olusegun Aina', '8034315211': 'Olatunde Sowunmi', '9039231107': 'Joshua Samuel', '8061572906': 'Uwem Mkpong Archibong', '7080858791': 'Uchenna Ohaeri PMP', '8036197738': 'Aromeh Sunday Adole', '8027291738': 'Christwealth Kolawole', '8037829881': 'Maharaz Saad', '8069680993': 'Orkuma Anyoko - Shaba', '8039689404': 'Wilson Obidah, PhD', '8035672752': 'Victoria', '9036683244': 'Musari Mathew', '8060895366': 'Musari Mathew', '8032825342': 'Engr.Olatunde Michael Ibrahim', '8188541950': 'Engr.Olatunde Michael Ibrahim', '8051500690': 'Osinuga Rahman', '8062411073': 'Bala, Sunday', '8066789611': 'Leonard Nzenwa', '8032195105': 'Dr.Victor Evans.', '8058434421': 'Jatto Osabuhen Jonathan', '8056488800': 'Akinbebije Damilola', '8033597679': 'Mr. Adigun Oluwamayowa Oluwaseun Kingsley', '8035881242': 'Emmanuel Akissa', '8029147144': 'Pam Dung Kim', '8023152210': 'Oke Olabamiji', '8036206061': ' Oke Olabamiji', '8033015230': ' AKINLAMILO, ELLIOT OLAFISOYE', '8069766002': 'Ahmad Yahuza Getso',  '8072661313': 'Alaghala, Alphons L', '8037257819': 'OSUJI ALBERTO OBINNA', '8035983539': 'Shitery Aaron Istifanus', '8035691309': 'Olusegun Adepoju', '8033496839': 'Dr. Charles Anosike FCMI, MNIM GPM', '8032007440': 'Mr.Erere Oyibo - Rhokaye', '8032479757': 'Aiyedun Olubunm FCIS, MTM', '8022449020': 'Akubueze Chibuzo H.', '8030618326': 'D.Tola Winjobi, PhD', '8082008222': 'D.Tola Winjobi, PhD', '8036469928': 'Mohammed Saeed Suleiman', '8068056242': 'Markus Njidda Uba', '8055928327': 'Rev. Sr. Paulette Ekejiuba, PhD', '8144513831': 'Comrade DR Mk Adam Rano (Dr Muhammad Kabir Adam)', '8086633083': 'Kayode Akintolu', '8037093585': 'Nkem Joseph-Palmer', '9023924412': 'Nkem Joseph-Palmer', '8023204138': 'Elvis Onuora FCA, FCTI', '8052913643': 'Abimbola Omolabi PhD', '8033172828': 'Abimbola Omolabi PhD', '8052448149': 'JOSEPH HUMPHREY KABE', '7039554117': 'Job Ayodele Ekundayo', '8033865790': 'Prof. Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart', '8036005365': 'Muhammad Kachallah', '8034106448': 'Lizzy Igbine Mrs.', '8033778222': 'Frederick Bethel Saduwa', '8033341079': 'ISERE Joseph', '8173245448': 'Shirley Ehru Nehemiah', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '7084415597': 'Ismaila Haliru Zarma', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', '7036481502': 'Eni Okoi, Esq.', '8149575705': 'Sylvester Ejiofor', '8032601105': 'Hon. Anselm C. Onuorah', '7069551267': 'Beeson Lawson', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '8037875416': 'Adeniyi Aturamu MNIOB ', '8098449890': 'Adeniyi Aturamu MNIOB ', '7032220542': 'PIUS IPUOLE', '8033341416': 'OLANIRAN ADERIBIGBE', '8036754537': 'Ogechukwu Eucharia Maduka', '8062862692': 'Victor Bisong', '8037879235': 'Zuhair Jibril', '7060772784': 'Victor Obioma Uche', '8033344595': 'Oladejobi Godwin Adebola', '8033156025': 'Engr Aishatu Aliyu Umar, FNSE', '8095000000': 'Engr Aishatu Aliyu Umar, FNSE', '8163686103': 'Dr. Ola Adigun-daniels', '8061296216': 'Godwin Okoko', '8030824948': 'Ogunmefun Toyin', '8131538812': 'SP Onyejegbu Basilia Cynthia', '7088607443': 'Prince Amaefula', '8037012676': 'Oyinloye Oyedele P.'}

#

class WhatsappAndroidTests(unittest.TestCase):
    reminder_ = """*Gentle Reminder: Certification for Chartered Management Status Holds As Planned*
{} {},

Please, be reminded that the scheduled Certification/Induction for Chartered Management Status will hold as planned in Lagos, Nigeria as follows::

Lagos:

Date: *Thursday, 16th December, 2021.*

Time: *11.00am prompt.*

Venue: *Lagos Chamber of Commerce and Industry (LCCI) Conference and Exhibition Centre,*

Plot 10, Nurudeen Olowopopo Street, Behind MKO, Abiola Garden, Alausa, Lagos.

Please Note: There would be *no Abuja session* this time instead we have made arrangements for those who may not make it to *participate virtually*. Please notify us if you would be participating physically or virtually.


There is provision for you to make payment and, or to complete your registration at the venue, in case you have not done yours.

We are available to respond to further inquiries.

We shall be expecting you.
Many thanks and best regards.

*Michael Adewole Okara*, (ChMC, FIMC, CMC, arpa)
Board Representative.
+2348035796502 | mcscglobal.org"""

    reminder = """*Gentle Reminder: Registration Package (Forms) | Event Details*
    
{} {},

Please, find attached our registration forms.     
Please fill as appropriate: starting from degree level to professional level and work experience; attach your profile and revert to us ASAP so we can commence the registration process right away.
 
Please see event dates and other details below:

Lagos:
Date: Wednesday, 6th October, 2021.
Time: 11.00am prompt.
Venue: Training Hall 3, First Floor,
Lagos Chamber of Commerce and Industry (LCCI) Conference and Exhibition Centre, Plot 10, Nurudeen Olowopopo Street, Behind MKO, Abiola Garden, Alausa, Lagos.

Abuja:
Date: Wednesday, 13th October, 2021.
Time: 11.00am prompt.
Venue: Silk Road Restaurant, Sinoki House,
5th Floor, Plot 770, Off Samuel Ademulegun Avenue, Opp. Federal Ministry of Transport, CBD, Abuja-FCT.

Many thanks and best regards,

Michael Adewole Okara, (ChMC, FIMC, CMC, arpa)
Board Representative.
+2348035796502 | mcscglobal.org"""
    def setUp(self):
        desired_caps ={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'DEFFL19801000067'
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
            msg_txt.send_keys(self.reminder_.format(salute, contacts[phone]))
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
    for phone in contacts.keys():
        suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappAndroidTests)
        unittest.TextTestRunner(verbosity=1).run(suite)
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



