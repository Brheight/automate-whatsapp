import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
not_found = {}
count = 0
#'8037875416':
#'215-329-4154': 'Claudia Gale ',  '215-329-4154': 'Claudia Gale ',  '215-329-4154': 'Claudia Gale ', '215-329-4154': 'Claudia Gale ',
# '8022449020': 'Akubueze Chibuzo H.',
#not found '7038402601': 'ALEXANDER IFEANYI OGOLO', ' 08059453568': 'ALEXANDER IFEANYI OGOLO', '802 324 5490': 'Debbie Akwara',
#deferred '8106411038': 'Olusola Gbadamosi\t\t', ' 08062638111': 'Olusola Gbadamosi\t\t','8106411038': 'Olusola Gbadamosi\t\t', ' 08062638111': 'Olusola Gbadamosi\t\t', '8106411038': 'Olusola Gbadamosi', '8062638111': 'Olusola Gbadamosi','8106411038': 'Olusola Gbadamosi', '8062638111': 'Olusola Gbadamosi', '08106411038, 08062638111': 'Olusola Gbadamosi\t\t', '8106411038': 'Olusola Gbadamosi\t\t', ' 08062638111': 'Olusola Gbadamosi\t\t',
#'8029147144': 'Pam Dung Kim',
#called abuja march reminders  '8069766002': 'Ahmad Yahuza Getso','8069766002': 'Ahmad Yahuza Getso','8069766002': 'Ahmad Yahuza Getso','8069766002': 'Ahmad Yahuza Getso',  '8069766002': 'Ahmad Yahuza Getso', '8069766002': 'Ahmad Yahuza Getso', '8069766002': 'Ahmad Yahuza Getso',
#not found {'8037879235': 'Zuhair Jibril', '8163686103': 'Dr. Ola Adigun-daniels', '8030824948': 'Ogunmefun Toyin', '8037012676': 'Oyinloye Oyedele P.'}
#not found {'8023152210': 'Oke Olabamiji', '8036206061': ' Oke Olabamiji', '8023204138': 'Elvis Onuora FCA, FCTI', '8052913643': 'Abimbola Omolabi PhD', '8033341079': 'ISERE Joseph', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', '7069551267': 'Beeson Lawson', '7032220542': 'PIUS IPUOLE', '8037879235': 'Zuhair Jibril'}

class WhatsappAndroidTests():
    #'+2347046383713, +2347046216417': 'Sina Sofola, SAN',   '8034373712': "Ugwuoke Emeka Emmanuel':",'08034373712': "Ugwuoke Emeka Emmanuel':",  '+2347046383713': 'Sina Sofola, SAN', ' +2347046216417': 'Sina Sofola, SAN', '8034373712': "Ugwuoke Emeka Emmanuel':",'7046383713': 'Sina Sofola, SAN', ' 7046216417': 'Sina Sofola, SAN', '8034373712': "Ugwuoke Emeka Emmanuel':",
    #not found {'7060772784': 'Victor Obioma Uche', '8061296216': 'Godwin Okoko', '8035446978': 'Promise Nwafor A Anelechi', '8064499724': 'Mr. S. Kola Adekoya', '9097512017': 'Dr.Ashikia Festus Uwakhemen', '9028888903': 'Ikechukwu Oliobi'}
    #not found{'9039231107': 'Joshua Samuel', '8061572906': 'Uwem Mkpong Archibong', '8036197738': 'Aromeh Sunday Adole'}
    #sent'7066282414':'Bright Ofeyi',
    #'7046383713': 'Sina Sofola, SAN', ' 7046216417': 'Sina Sofola, SAN',
    #
    #new response via email = deferred  '+254722599621': 'Peter Okeyo Oraro', '+254 722 599 621': 'Peter Okeyo Oraro', '+254 722 599 621': 'Peter Okeyo Oraro','+254 722 599 621': 'Peter Okeyo Oraro', '+254 722 599 621': 'Peter Okeyo Oraro', '+254722599621': 'Peter Okeyo Oraro',
    # '803 716 9795': 'West Pamela Inkobat','803 716 9795': 'West Pamela Inkobat','0803 716 9795': 'West Pamela Inkobat', '803 716 9795': 'West Pamela Inkobat', deferred
    #deferred march 22  '8168755195': 'Ahmed Yakubu Kamaldeen', '8023580925': 'Ahmed Yakubu Kamaldeen','8168755195': 'Ahmed Yakubu Kamaldeen', ' 08023580925': 'Ahmed Yakubu Kamaldeen', '8168755195': 'Ahmed Yakubu Kamaldeen', '8023580925': 'Ahmed Yakubu Kamaldeen', '08168755195, 08023580925': 'Ahmed Yakubu Kamaldeen', '8168755195': 'Ahmed Yakubu Kamaldeen', ' 08023580925': 'Ahmed Yakubu Kamaldeen', '8168755195': 'Ahmed Yakubu Kamaldeen', ' 08023580925': 'Ahmed Yakubu Kamaldeen',
    #sent march lage
    #
    #
    #
    #
    #already sent
    #send for june = {'7060772784': 'Victor Obioma Uche','8060895366': 'Busari Matthew','8032825342': 'Engr Olatunde Micheal IBRAHIM','8188541950': 'Engr Olatunde Micheal IBRAHIM','8058434421': 'Jatto Osabuhen Jonathan', '8033597679': 'Mr. Adigun Oluwamayowa Oluwaseun','8023152210': 'Oke Olabamiji','8036206061': ' Oke Olabamiji', '8033015230': ' Akinlamilo Elliot Olafisoye','8035691309': 'Olusegun Adepoju','8068056242': 'Markus Njidda Uba ','8086633083': 'Kayode Ibrahim AKINTOLU','9023924412': 'Nkem Joseph-Palmer ','8023204138': 'Elvis Onuora FCA, FCTI','8052913643': 'Abimbola Omolabi PhD','8033172828': 'Abimbola Omolabi PhD','8052448149': 'JOSEPH HUMPHREY KABE','8036005365': 'Muhammad Kachallah', '8033341079': 'ISERE Joseph','906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara','new tes':'new test','+48669784338': ' Dr. James Onyinye Mbakpou', '+375299641852': ' Dr. James Onyinye Mbakpou', '8022226864': 'Onalu Uchenna . C','8037003649': 'HASSAN SALIHU ANKA ', '7088607443': 'Prince Amaefula', '8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia', '8030824948': 'Ogunmefun Toyin', '7036481502': 'Eni Okoi, Esq', ' 8173078252': 'Peter Imafidon Omokaro','8055266838': 'PETER OMOKARO MBA, FIMC,CMC,FCIB ', '8033886655 ': 'Seun Sodipe ', '8172925952': 'Seun Sodipe ', '8027862387': 'Austin Itsoya Momodu', '8028911399': 'Markus Njidda Uba ', '8035881242': 'Emmanuel Akissa','8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ', '8023361732': 'Prof. Kessington Obahiagbon', '6472030350': 'Prof. Adefemi Olokesusi (Ph.D)','8037008618': 'KALU, Peters PhD', '+233200429430': 'Kenneth Igiri ', ' +233544904920': 'Kenneth Igiri ', '8062279615': 'Dr. John Oladejo', '810739-2731': 'Dr Oluchi John-Isiodu', '94615700': 'Amin Abubakar Sadiq ', '8023935869': 'Amin Abubakar Sadiq ','7038402601': 'ALEXANDER IFEANYI OGOLO', '8059453568': 'ALEXANDER IFEANYI OGOLO', '8023245490': 'Debbie Akwara', '7068490339': 'Titilayo Wumi Oluwafemi', '8035136609': 'Stephen Bamidele Ogodo', '255627542057': 'Ernest Masasi','8189624547': 'Benson Ndaji ', '8064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '8037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO','7033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '8052362288': 'Moses Mogbolu ', '8159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', '+447512093697': 'Ayodapo Oyebade ', '+447824798888': 'Ayodapo Oyebade ', '+447043050050': 'Ayodapo Oyebade ', '146140167': 'Victoria Alonge ', '7359948': 'Victoria Alonge ', '8023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', '7031042122': 'Oyegoke Adekunle Alani', '8173015230': ' Akinlamilo Elliot Olafisoye', '8033015230': ' Akinlamilo Elliot Olafisoye','8037012676': 'Oyinloye Oyedele P.', '9029461146 ': 'Oyinloye Oyedele P.', '+256417201019': 'Adekemi Ndieli ', '+256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O','8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '9037808592': 'Engr. Benjamin Eboehi', '8035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '8061296216': 'Godwin Okoko ', '8133943520': '"Oluwole Olukoya" ', '7032220542': 'PIUS IPUOLE ', '8032327228': 'Prof Samuel Ogunwale Ogundiran', '8030917088': 'Prof Samuel Ogunwale Ogundiran', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '8034932689': 'LAWSON BEESON ', '7069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '8032601105': 'Hon. Anselm C. Onuorah'}
    #sent june '8023361732': 'Prof. Kessington Obahiagbon', '8037010777': 'Rev. Jim Piomoki-Stevens', '(647) 203-0350': 'Prof. Adefemi Olokesusi (Ph.D)', '8037008618': 'KALU, Peters PhD', '+233 200 429 430': 'Kenneth Igiri ', ' +233 544 904 920': 'Kenneth Igiri ', '8033165162': 'Terseer Ugbor ', '8083889629': 'Dr. Effiong Okon Ekaeba', '8062279615': 'Dr. John Oladejo', '810739-2731': 'Dr Oluchi John-Isiodu', '7034054962': 'Adeniyi Salaudeen', ' (9) 4615700': 'Amin Abubakar Sadiq ', ' 8023935869': 'Amin Abubakar Sadiq ', '(0)80 9099 8811': 'Adaobi Ekweanya ', '803 309 5945': 'Helen Tamunoibelema ',
    #march june abuja  reminde{ '8033344595': 'Oladejobi Godwin Adebola', '8033156025': 'Engr Aishatu Aliyu Umar, FNSE', '8095000000': 'Engr Aishatu Aliyu Umar, FNSE', '8163686103': 'Dr. Ola Adigun-daniels', '8061296216': 'Godwin Okoko', '8030824948': 'Ogunmefun Toyin', '8131538812': 'SP Onyejegbu Basilia Cynthia', '7088607443': 'Prince Amaefula', '8037012676': 'Oyinloye Oyedele P.', '8035446978': 'Promise Nwafor A Anelechi', '+256771003594': ' Adekemi Ndieli', '8064499724': 'Mr. S. Kola Adekoya','8023204661': 'AZUBUIKE CHIDOZIE OKONKWO','8034240632': 'Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc', '8072599298': ' Tpl Adeyemo Olajide Kamoru JP, fnitp, fimc','9097512017': 'Dr.Ashikia Festus Uwakhemen', '8033509752': 'Idumonza Isidahomhen', '8030717044': 'Derek Omoleh', '8033118894': 'Igenegbai Christiana Joy', '8034373712': 'Ugwuoke Emeka Emmanuel', '8033518361': 'Ikechukwu Oliobi', '9028888903': 'Ikechukwu Oliobi', '8034551482': 'George Chinonso - Obi','7067941550': 'Bldr.Alvary A.Durkwa', '8023245490': 'Debbie Akwara', '8067742773': 'Mr.Awusa Peter Ewa', '8035693740': 'Prince Bola Olusegun Aina', '8034315211': 'Olatunde Sowunmi', '9039231107': 'Joshua Samuel', '8061572906': 'Uwem Mkpong Archibong', '7080858791': 'Uchenna Ohaeri PMP',}
    # abuja june duplicated contacts ={'8052913643': 'Abimbola Omolabi PhD', '8033172828': 'Abimbola Omolabi PhD', '8052448149': 'JOSEPH HUMPHREY KABE', '8036005365': 'Muhammad Kachallah', '8033341079': 'ISERE Joseph', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', 'new tes': 'new test', '+48669784338': ' Dr. James Onyinye Mbakpou', '+375299641852': ' Dr. James Onyinye Mbakpou', '8022226864': 'Onalu Uchenna . C', '8037003649': 'HASSAN SALIHU ANKA ',  '7088607443': 'Prince Amaefula', '8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia', '8030824948': 'Ogunmefun Toyin', '7036481502': 'Eni Okoi, Esq', ' 8173078252': 'Peter Imafidon Omokaro', '8055266838': 'PETER OMOKARO MBA, FIMC,CMC,FCIB ', '8033886655 ': 'Seun Sodipe ', '8172925952': 'Seun Sodipe ', '8027862387': 'Austin Itsoya Momodu', '8028911399': 'Markus Njidda Uba ', '8035881242': 'Emmanuel Akissa', '8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ', '8023361732': 'Prof. Kessington Obahiagbon', '6472030350': 'Prof. Adefemi Olokesusi (Ph.D)', '8037008618': 'KALU, Peters PhD', '+233200429430': 'Kenneth Igiri ', ' +233544904920': 'Kenneth Igiri ', '8062279615': 'Dr. John Oladejo', '810739-2731': 'Dr Oluchi John-Isiodu', '94615700': 'Amin Abubakar Sadiq ', '8023935869': 'Amin Abubakar Sadiq ', '7038402601': 'ALEXANDER IFEANYI OGOLO', '8059453568': 'ALEXANDER IFEANYI OGOLO', '8023245490': 'Debbie Akwara', '7068490339': 'Titilayo Wumi Oluwafemi', '8035136609': 'Stephen Bamidele Ogodo', '255627542057': 'Ernest Masasi', '8189624547': 'Benson Ndaji ', '8064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '8037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO', '7033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '8052362288': 'Moses Mogbolu ', '8159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', '+447512093697': 'Ayodapo Oyebade ', '+447824798888': 'Ayodapo Oyebade ', '+447043050050': 'Ayodapo Oyebade ', '146140167': 'Victoria Alonge ', '7359948': 'Victoria Alonge ', '8023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', '7031042122': 'Oyegoke Adekunle Alani', '8173015230': ' Akinlamilo Elliot Olafisoye', '8037012676': 'Oyinloye Oyedele P.', '9029461146 ': 'Oyinloye Oyedele P.', '+256417201019': 'Adekemi Ndieli ', '+256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O', '8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '9037808592': 'Engr. Benjamin Eboehi', '8035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '8061296216': 'Godwin Okoko ', '8133943520': '"Oluwole Olukoya" ', '7032220542': 'PIUS IPUOLE ', '8032327228': 'Prof Samuel Ogunwale Ogundiran', '8030917088': 'Prof Samuel Ogunwale Ogundiran', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '8034932689': 'LAWSON BEESON ', '7069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '8032601105': 'Hon. Anselm C. Onuorah'}
    #sent  june abuja'8062625402': 'Maikudi Ibrahim Abubakar', '7030834395': 'Engr. Mahraz Karaye', '7068490339': 'Titilayo Wumi Oluwafemi', '8035136609': 'Stephen Bamidele Ogodo', ' 09098109072': 'Stephen Bamidele Ogodo', '8060740202': 'Dr. Alhaji Musa Liman', '7038080616': 'Lovelyn Okoye', '255627542057': 'Ernest Masasi', '8033145174': 'Dominic Okafor ', '+447741368789 ': 'Salisu Uba ', '8189624547': 'Benson Ndaji ', ' 8064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '8037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO,', '7033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '8052362288': 'Moses Mogbolu ', ' 8159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', '  +44 7512 093697': 'Ayodapo Oyebade ', ' +44 7824 798888': 'Ayodapo Oyebade ', ' +44 7043 050050': 'Ayodapo Oyebade ',  '-1-4614016-7': 'Victoria Alonge ', ' 7359948': 'Victoria Alonge ', ' 8023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', 'george.obi@singeobigroup.com': '"George Obi" ', '7031042122': 'Oyegoke Adekunle Alani', '8173015230': ' Akinlamilo Elliot Olafisoye',  '+2438037012676': 'Oyinloye Oyedele P.', ' +2439029461146 ': 'Oyinloye Oyedele P.', '+256 417 201 019': 'Adekemi Ndieli ', ' +256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O', '8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '9037808592': 'Engr. Benjamin Eboehi', ' 08035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '8061296216': 'Godwin Okoko ', '8133943520': '"Oluwole Olukoya" ', '7032220542': 'PIUS IPUOLE ', '8032327228': 'Prof Samuel Ogunwale Ogundiran', ' 08030917088': 'Prof Samuel Ogunwale Ogundiran', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '803 493 2689': 'LAWSON BEESON ', '7069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '8032601105': 'Hon. Anselm C. Onuorah', '8024260942': 'Gidado Tahir ', '8036469928': 'Mohammed Saeed Suleiman ', ' 08098469928': 'Mohammed Saeed Suleiman ', '8036754537': 'Ogechukwu Eucharia Maduka', '1. (+234) (1) 2954690 2': 'Adeyinka Adegbite, Esq', ' (+234) (1) 2954691 3': 'Adeyinka Adegbite, Esq', ' (+234)9053333393': 'Adeyinka Adegbite, Esq', '8056659371': 'Dr. Olotu, O. Ayopo', ' 08098929477': 'Dr. Olotu, O. Ayopo', '8062862692': 'Victor Bisong', '7084415597': 'Ismaila Haliru Zarma', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '8035995868': 'Hawa BenHirki ', ' (1) 2713990 ': 'Kayode Ibrahim AKINTOLU',  ' 810 375 6894': 'Reginald Udenze Ihedike', '7039554117': ' Job Ayodele Ekundayo', '7060772784': 'Victor Obioma Uche', '8033865790': 'Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart ','8033778222': 'Frederick Bethel Saduwa ', ' (0) 803 334 1079 ': 'Joseph Isere ', ' 07068600006 ': 'Kennedy Akpan', ' 09027936331': 'Kennedy Akpan', '8056038074': 'ONABEKUN ADEKUNLE ', ' 702540721': 'ONABEKUN ADEKUNLE ', ' -7037905644 ': 'Idornigie Ide Christopher ', ' 08071827748': 'Idornigie Ide Christopher ', '8038442908': 'Emmanuel Olawuyi ', ' +27 12 394 1158': 'Nthabiseng Maude Mthethwa(DBA)Hon.', ' +27 82 635 1627': 'Nthabiseng Maude Mthethwa(DBA)Hon.',  '8033815239': 'Chukwuka Egbule (M.Sc., FCA, FCTI)', ' 08058448143 ': 'Chukwuka Egbule (M.Sc., FCA, FCTI)',  '8033509752': 'Idumonza Isidahomhen ',  ' -08033172828': 'Abimbola Omolabi PhD', '8094773839': 'Francois Hounda DOSSOU', '8037093585': 'Nkem Joseph-Palmer ',  ' 07046852104': 'Nkem Joseph-Palmer ', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7020677189': 'Ndubuwa Ugwunna Victor', '9087259465': 'Engr Jane Ifeoma Kamanya', '8144513831': 'Dr Muhammad Kabir Adam', ' 0708160': 'Dr Muhammad Kabir Adam', '8064657799': 'Dr Joseph Rankin', '8102875997': 'Dr Joseph Rankin', '8032479757': 'Aiyedun Olubunm Fcis Mtm', '712187260': 'Dr Kasozi Nathan', ' 0702916735': 'Dr Kasozi Nathan', '7035466027': 'Emmanuel Oladipo Akogun ', '8069317779': 'Titi Yakubu ', '8033156025 ': 'Engr Aishatu Aliyu Umar, FNSE', ' 08095000000': 'Engr Aishatu Aliyu Umar, FNSE', '8033107505': 'Mrs Juliet Ogedi David-west', '8065660093': 'Roselyn Eneji', ' 803 4071 116': 'Paul Nnamah ', '8055076706': 'Olajide Ojo ', '904530629': 'Abayomi Bello', '8039689404': 'WILSON OBIDAH, PhD', '8033496839': 'Dr. Charles Anosike FCMI MNIM GPM', '8033613144': 'Ujunwa Rosemary Felicia (Mrs)', ' 8055266838': 'Peter Imafidon Omokaro', '8062611560': 'Olusegun Adepoju', '8032007440': 'Erere Oyibo-Rhokaye ', '8033467900': 'Dr. Chukwunonso Izuchukwu Pharm.d Cmc Fimc', '8055928327': 'Rev. Sr. Paulette Ekejiuba Phd', '8037109285': 'Ndifreke Andrew-essien', '8033335091': 'Barr. Miss Chigozie Ifeoma Nwagbara',' 07088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', ' 08156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara',
    #sent june abuja '8128678873': 'Mr. Aniefiok E. Thomas', '+23279881111\xa0 ': 'Dipo Gbenro ', '+23276368  359': 'Dipo Gbenro ', '+447443423890': 'Uchennia Akahalu ', '7067941550': 'Bldr. Alvary A. Durkwa', '8030717044': 'Derek Omoleh ', '8055427409': 'Uchenna A. Okoroafor', '8032195105': 'Dr. Victor Evans', '8056488800': 'Akinbebije Damilola', '8035983539': 'Shitery Aaron Istifanus', '8066789611': 'Leonard Nzenwa ', '8062411073': 'Sunday Bala ', '9036683244': 'Busari Matthew', '8060895366': 'Busari Matthew', '7080858791': 'Uchenna Solomon Ohaeri ', '9039231107': 'Joshua Samuel', '7011990709': 'Ogunbiyi-davies Biodun Abiola', '8051500690': ' Osinuga Rahman', '8111312517': 'Eluozo Collins ', '8034531431': 'Olajire Adebayo Aderemi', '9097512017': 'Ashikia Festus Uwakhemen', '8163686103': 'Dr. Ola Adigun-Daniels', '8069680993': 'Orkuma Emmanuel Anyoko-Shaba', '8037829881': 'Maharaz Saad', '8027291738': 'CHRISTWEALTH Kolawole Olusola', '8036197738': 'Aromeh Sunday Adole', '8037262350': 'George Idiaghe', '8061572906': 'Uwem Mkpong  Archibong', '8033047278': 'Nasamu Ibrahim', '8034315211': 'Olatunde Sowunmi', '8067742773': 'Mr. Awusa Peter Ewa', '8033118894': ' Igenegbai Christiana Joy', '8035677488': 'Ekemezie Okechukwu '
    contacts={'\t7031384185': 'Adewale Davies Owoyemi\t', ' 08023012752': 'Adewale Davies Owoyemi\t','8022226864': 'Onalu Uchenna . C\t\t','8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke\t', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia\t', '8030824948': 'Ogunmefun Toyin\t', '8033341416': 'OLANIRAN ADERIBIGBE', '8033156117': 'Umar B. Bindir', '8173245448': 'Shirley Ehru Nehemiah', '8037879235': 'Dr ZUHAIR JIBIR ',  '7036481502': 'Eni Okoi, Esq', '8033078252': 'Peter Imafidon Omokaro', ' 8173078252': 'Peter Imafidon Omokaro', '8055266838': 'PETER OMOKARO MBA, FIMC,CMC,FCIB ', ' 8033886655 ': 'Seun Sodipe ', ' 8172925952': 'Seun Sodipe ', '8027862387': 'Austin Itsoya Momodu', '': 'Markus Njidda Uba ', ' (0)8028911399': 'Markus Njidda Uba ',  '8035881242': 'Emmanuel Akissa', '8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ','8033483674': 'Essang Paddy\t',  '7088607443': 'Prince Amaefula\t\t', '8080767155': 'Chukwudi Iwuozor\t\t','8037003649': 'HASSAN SALIHU ANKA ', '8034746507': 'Barr Lohor Alexander\t\t','7039094177': 'Chris Manuawuchukwu  Agu','+48572537567': ' Dr. James Onyinye Mbakpou', ' +48669784338': ' Dr. James Onyinye Mbakpou', ' +375299641852': ' Dr. James Onyinye Mbakpou','8033377261': 'Prof. Basil O. Nwosu','8060941944': 'Sir. Stephen O. Enike-Matthew','8171270027': 'Sir. Stephen O. Enike-Matthew','8035028205': 'Akpe Oyinkarebai Michael', '8037879235': 'Zuhair Jibril','8023361732': 'Prof. Kessington Obahiagbon', '8052362288': 'Moses Mogbolu', '8159552222': ' Moses Mogbolu',}
    #old june { '8036197738': 'Aromeh Sunday Adole', '8027291738': 'Christwealth Kolawole','8037829881': 'Maharaz Saad', '8069680993': 'Orkuma Anyoko - Shaba', '8039689404': 'Wilson Obidah, PhD', '8035672752': 'Victoria', '9036683244': 'Musari Mathew', '8060895366': 'Musari Mathew', '8032825342': 'Engr.Olatunde Michael Ibrahim', '8188541950': 'Engr.Olatunde Michael Ibrahim', '8051500690': 'Osinuga Rahman', '8062411073': 'Bala, Sunday', '8066789611': 'Leonard Nzenwa', '8032195105': 'Dr.Victor Evans.', '8058434421': 'Jatto Osabuhen Jonathan', '8056488800': 'Akinbebije Damilola', '8033597679': 'Mr. Adigun Oluwamayowa Oluwaseun Kingsley', '8035881242': 'Emmanuel Akissa',  '8023152210': 'Oke Olabamiji', '8036206061': ' Oke Olabamiji', '8033015230': ' AKINLAMILO, ELLIOT OLAFISOYE',  '8037257819': 'OSUJI ALBERTO OBINNA', '8035983539': 'Shitery Aaron Istifanus', '8035691309': 'Olusegun Adepoju', '8033496839': 'Dr. Charles Anosike FCMI, MNIM GPM', '8032007440': 'Mr.Erere Oyibo - Rhokaye', '8032479757': 'Aiyedun Olubunm FCIS, MTM','8036469928': 'Mohammed Saeed Suleiman', '8068056242': 'Markus Njidda Uba', '8055928327': 'Rev. Sr. Paulette Ekejiuba, PhD', '8144513831': 'Comrade DR Mk Adam Rano (Dr Muhammad Kabir Adam)', '8086633083': 'Kayode Akintolu', '8037093585': 'Nkem Joseph-Palmer', '9023924412': 'Nkem Joseph-Palmer', '8023204138': 'Elvis Onuora FCA, FCTI', '8052913643': 'Abimbola Omolabi PhD', '8033172828': 'Abimbola Omolabi PhD', '8052448149': 'JOSEPH HUMPHREY KABE', '7039554117': 'Job Ayodele Ekundayo', '8033865790': 'Prof. Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart', '8036005365': 'Muhammad Kachallah',  '8033778222': 'Frederick Bethel Saduwa', '8033341079': 'ISERE Joseph', '8173245448': 'Shirley Ehru Nehemiah', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '7084415597': 'Ismaila Haliru Zarma', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', '7036481502': 'Eni Okoi, Esq.','8032601105': 'Hon. Anselm C. Onuorah', '7069551267': 'Beeson Lawson', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM',   '7032220542': 'PIUS IPUOLE', '8033341416': 'OLANIRAN ADERIBIGBE', '8036754537': 'Ogechukwu Eucharia Maduka', '8062862692': 'Victor Bisong',}
    regpack = """*Gentle Reminder: Certification for Chartered Management Status Holds As Planned*

Distinguished Awardee,

Please, be reminded that the scheduled Certification/Induction for Chartered Management Status will hold as planned: :
*Abuja (Physical)*:

Date: Thursday, 10th March, 2022.

Time: 11.00am prompt.

Venue: Silk Road Restaurant, Sinoki House,

5th Floor, Plot 770, Off Samuel Ademulegun Avenue, Opp. Federal Ministry of Transport, CBD, Abuja-FCT.

*Virtual (merged with Abuja)*:
Date: Thursday, 10th March, 2022.

Time: 11.00am prompt.

There is provision for you to make payment and, or to complete your registration at the venue, in case you have not done yours.

We are available to respond to further inquiries.

We shall be expecting you.

   
Michael Adewole Okara, (ChMC, FIMC, CMC, FIMS, arpa)

Board Representative.

+2348035796502 | mcscglobal.org

"""

    _regpack_ = """*Gentle Reminder: Registration Package (Register Online)*
    
{} {},
  
Please, be reminded that we await your filled CIMC registration/application package which authenticates your acceptance of our CIMC Certification chartered management consultant status (award) offer. You can now fill the forms online with the link below:

https://mcscglobal.org/forms.html

Should you need any clarification on how to fill the forms or on any other matter, please, feel free to reach us. We are very much on hand to attend to you. Also, please endeavor to advise us as soon as you make payment. Although payment may be made at the event venue, it is preferable if made much earlier. Early payment gives us ample time to customize materials to your details as well as to possibly process your certificate ahead of time. You may request for payment advice if you do not have the complete details.

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
    reminder = """*Gentle Reminder: March Event (Physical and Virtual)*
    
{} {},

Trust you are having a splendid day. We understand that you could not make it for the last event. It gives us great joy to inform you that our next event has been scheduled for the month of March to hold on the 3rd in Lagos (Physical and Virtual) and on the 10th in Abuja (Physical). 
Please indicate your preference on your revert. The next stage is to proceed to payment and registration. Although payment may be made at the event venue / event day, it is preferable if made much earlier. Early payment gives us ample time to customize materials to your details as well as to possibly process your certificate ahead of time. You may request for payment advice if you do not have the complete details. 
We hope you would be better disposed this time. Following your response we shall follow up this mail with your letter of invite and registration package.

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
            print('sent', 'count','name:', self.contacts[phone], 'phone:',phone)
            print('not found', not_found)
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
        except Exception as e:
            print(e, 'count', ': Not found', self.contacts[phone], phone)
            not_found[phone]= self.contacts[phone]
            print('not found', not_found)



if __name__ == '__main__':
    #WhatsappAndroidTests().setUp()
    WhatsappAndroidTests().start()
    pass
new_contact ={'08035028205': 'Akpe Oyinkarebai Michael', '07039094177': 'Chris Manuawuchukwu  Agu', '+48572537567, +48669784338, +375299641852': ' Dr. James Onyinye Mbakpou', '08022226864': 'Onalu Uchenna . C\t\t', '8037003649': 'HASSAN SALIHU ANKA ', '\t7031384185, 08023012752': 'Adewale Davies Owoyemi\t', '8034746507': 'Barr Lohor Alexander\t\t', '8033483674': 'Essang Paddy\t','7088607443': 'Prince Amaefula\t\t', '8080767155': 'Chukwudi Iwuozor\t\t', '8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke\t', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia\t', '8030824948': 'Ogunmefun Toyin\t', '8033341416': 'OLANIRAN ADERIBIGBE', '8033156117': 'Umar B. Bindir', '8173245448': 'Shirley Ehru Nehemiah', '8037879235': 'Dr ZUHAIR JIBIR ', '+2348060941944 | +2348171270027': 'Sir. Stephen O. Enike-Matthew,', '7036481502': 'Eni Okoi, Esq', '+2348033078252, +2348173078252,+2348055266838': 'PETER OMOKARO MBA, FIMC,CMC,FCIB ', '+234 8033886655 , +2348172925952': 'Seun Sodipe ', '8027862387': 'Austin Itsoya Momodu', ',+234 (0)8028911399,+234(0)8068056242': 'Markus Njidda Uba ', '8035881242': 'Emmanuel Akissa', '8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ', '8023361732': 'Prof. Kessington Obahiagbon', '08037010777': 'Rev. Jim Piomoki-Stevens', '(647) 203-0350': 'Prof. Adefemi Olokesusi (Ph.D)', '2348037008618': 'KALU, Peters PhD', '+233 200 429 430, +233 544 904 920': 'Kenneth Igiri ', '+2348033165162': 'Terseer Ugbor ', '8083889629': 'Dr. Effiong Okon Ekaeba', '8062279615': 'Dr. John Oladejo', '+234810739-2731': 'Dr Oluchi John-Isiodu', '2347034054962': 'Adeniyi Salaudeen', '+234 (9) 4615700, +2348023935869': 'Amin Abubakar Sadiq ', '+234(0)80 9099 8811': 'Adaobi Ekweanya ', '803 309 5945': 'Helen Tamunoibelema ', '07038402601, 08059453568': 'ALEXANDER IFEANYI OGOLO', '0802 324 5490': 'Debbie Akwara', '8062625402': 'Maikudi Ibrahim Abubakar', '7030834395': 'Engr. Mahraz Karaye', '7068490339': 'Titilayo Wumi Oluwafemi', '08035136609, 09098109072': 'Stephen Bamidele Ogodo', '8060740202': 'Dr. Alhaji Musa Liman', '7038080616': 'Lovelyn Okoye', '255627542057': 'Ernest Masasi', '2348033145174': 'Dominic Okafor ', '+447741368789 ': 'Salisu Uba ', '08189624547, 2348064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '+2348037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO,', '2347033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '+2348052362288, +2348159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', '  +44 7512 093697, +44 7824 798888, +44 7043 050050': 'Ayodapo Oyebade ', '+234-1-4614016-7, 7359948, +2348023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', 'george.obi@singeobigroup.com': '"George Obi" ', '7031042122': 'Oyegoke Adekunle Alani', '08173015230, 08033015230': ' Akinlamilo Elliot Olafisoye', '+2438037012676, +2439029461146 ': 'Oyinloye Oyedele P.', '+256 417 201 019, +256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O', '8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '09037808592, 08035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '8061296216': 'Godwin Okoko ', '8133943520': '"Oluwole Olukoya" ', '7032220542': 'PIUS IPUOLE ', '08032327228, 08030917088': 'Prof Samuel Ogunwale Ogundiran', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '234803 493 2689,+2347069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '2348032601105': 'Hon. Anselm C. Onuorah', '8024260942': 'Gidado Tahir ', '08036469928, 08098469928': 'Mohammed Saeed Suleiman ', '8036754537': 'Ogechukwu Eucharia Maduka', '1. (+234) (1) 2954690 2, (+234) (1) 2954691 3, (+234)9053333393': 'Adeyinka Adegbite, Esq', '08056659371, 08098929477': 'Dr. Olotu, O. Ayopo', '8062862692': 'Victor Bisong', '7084415597': 'Ismaila Haliru Zarma', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '8035995868': 'Hawa BenHirki ', '+234 (1) 2713990 , +2348086633083': 'Kayode Ibrahim AKINTOLU', '+234 810 375 6894': 'Reginald Udenze Ihedike', '+2347039554117': ' Job Ayodele Ekundayo', '7060772784': 'Victor Obioma Uche', '8033865790': 'Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart ', '8033778222': 'Frederick Bethel Saduwa ', '234 (0) 803 334 1079 ': 'Joseph Isere ', ' 07068600006 , 09027936331': 'Kennedy Akpan', '2348056038074, +234702540721': 'ONABEKUN ADEKUNLE ', ' +234-7037905644 , 08071827748': 'Idornigie Ide Christopher ', '08038442908': 'Emmanuel Olawuyi ', ' +27 12 394 1158, +27 82 635 1627': 'Nthabiseng Maude Mthethwa(DBA)Hon.', '08033815239, 08058448143 ': 'Chukwuka Egbule (M.Sc., FCA, FCTI)', ' (234) 8052448149': 'JOSEPH HUMPHREY KABE', '8033509752': 'Idumonza Isidahomhen ', '+234-08052913643, +234-08033172828': 'Abimbola Omolabi PhD', '08094773839': 'Francois Hounda DOSSOU', '08037093585, 09023924412, 07046852104': 'Nkem Joseph-Palmer ', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7020677189': 'Ndubuwa Ugwunna Victor', '9087259465': 'Engr Jane Ifeoma Kamanya', '08144513831, 0708160': 'Dr Muhammad Kabir Adam', '+2348064657799,+2348102875997': 'Dr Joseph Rankin', '8032479757': 'Aiyedun Olubunm Fcis Mtm', '0712187260, 0702916735': 'Dr Kasozi Nathan', '07035466027': 'Emmanuel Oladipo Akogun ', '08069317779': 'Titi Yakubu ', '08033156025 , 08095000000': 'Engr Aishatu Aliyu Umar, FNSE', '08033107505': 'Mrs Juliet Ogedi David-west', '8065660093': 'Roselyn Eneji', '+234 803 4071 116': 'Paul Nnamah ', '8055076706': 'Olajide Ojo ', '0904530629': 'Abayomi Bello', '08039689404': 'WILSON OBIDAH, PhD', '8033496839': 'Dr. Charles Anosike FCMI MNIM GPM', '8033613144': 'Ujunwa Rosemary Felicia (Mrs)', '+2348033078252, +2348173078252, +2348055266838': 'Peter Imafidon Omokaro', '8062611560': 'Olusegun Adepoju', '2348032007440': 'Erere Oyibo-Rhokaye ', '+2348033467900': 'Dr. Chukwunonso Izuchukwu Pharm.d Cmc Fimc', '8033377261': 'Prof. Basil O. Nwosu', '8055928327': 'Rev. Sr. Paulette Ekejiuba Phd', '+2348037109285': 'Ndifreke Andrew-essien', '08033335091, 07088932144, 08156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8128678873': 'Mr. Aniefiok E. Thomas', '+23279881111\xa0 ,+23276368  359': 'Dipo Gbenro ', '+447443423890': 'Uchennia Akahalu ', '+2347067941550': 'Bldr. Alvary A. Durkwa', '8030717044': 'Derek Omoleh ', '8055427409': 'Uchenna A. Okoroafor', '8032195105': 'Dr. Victor Evans', '8056488800': 'Akinbebije Damilola', '8035983539': 'Shitery Aaron Istifanus', '08066789611': 'Leonard Nzenwa ', '8062411073': 'Sunday Bala ', '+2349036683244, +2348060895366': 'Busari Matthew', '07080858791': 'Uchenna Solomon Ohaeri ', '2349039231107': 'Joshua Samuel', '7011990709': 'Ogunbiyi-davies Biodun Abiola', '8051500690': ' Osinuga Rahman', '8111312517': 'Eluozo Collins ', '23408032825342, 08188541950': 'Engr Olatunde Micheal IBRAHIM', '8034531431': 'Olajire Adebayo Aderemi', '9097512017': 'Ashikia Festus Uwakhemen', '8163686103': 'Dr. Ola Adigun-Daniels', '8069680993': 'Orkuma Emmanuel Anyoko-Shaba', '8037829881': 'Maharaz Saad', '8027291738': 'CHRISTWEALTH Kolawole Olusola', '08036197738': 'Aromeh Sunday Adole', '08037262350': 'George Idiaghe', '08061572906': 'Uwem Mkpong  Archibong', '08033047278': 'Nasamu Ibrahim', '08034315211': 'Olatunde Sowunmi', '08067742773': 'Mr. Awusa Peter Ewa', '08033118894': ' Igenegbai Christiana Joy', '8035677488': 'Ekemezie Okechukwu ',}
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


{'8035028205': 'Akpe Oyinkarebai Michael', '7039094177': 'Chris Manuawuchukwu  Agu',  '+48572537567': ' Dr. James Onyinye Mbakpou', ' +48669784338': ' Dr. James Onyinye Mbakpou', ' +375299641852': ' Dr. James Onyinye Mbakpou', '8022226864': 'Onalu Uchenna . C\t\t', '8037003649': 'HASSAN SALIHU ANKA ', '\t7031384185': 'Adewale Davies Owoyemi\t', ' 08023012752': 'Adewale Davies Owoyemi\t', '8034746507': 'Barr Lohor Alexander\t\t', '8033483674': 'Essang Paddy\t',  '7088607443': 'Prince Amaefula\t\t', '8080767155': 'Chukwudi Iwuozor\t\t', '8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke\t', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia\t', '8030824948': 'Ogunmefun Toyin\t', '8033341416': 'OLANIRAN ADERIBIGBE', '8033156117': 'Umar B. Bindir', '8173245448': 'Shirley Ehru Nehemiah', '8037879235': 'Dr ZUHAIR JIBIR ', '+2348060941944 | +2348171270027': 'Sir. Stephen O. Enike-Matthew,', '7036481502': 'Eni Okoi, Esq', '+2348033078252': 'Peter Imafidon Omokaro', ' +2348173078252': 'Peter Imafidon Omokaro', '+2348055266838': 'PETER OMOKARO MBA, FIMC,CMC,FCIB ', '+234 8033886655 ': 'Seun Sodipe ', ' +2348172925952': 'Seun Sodipe ', '8027862387': 'Austin Itsoya Momodu', '': 'Markus Njidda Uba ', '+234 (0)8028911399': 'Markus Njidda Uba ', '+234(0)8068056242': 'Markus Njidda Uba ', '8035881242': 'Emmanuel Akissa', '8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ', '8023361732': 'Prof. Kessington Obahiagbon', '8037010777': 'Rev. Jim Piomoki-Stevens', '(647) 203-0350': 'Prof. Adefemi Olokesusi (Ph.D)', '2348037008618': 'KALU, Peters PhD', '+233 200 429 430': 'Kenneth Igiri ', ' +233 544 904 920': 'Kenneth Igiri ', '+2348033165162': 'Terseer Ugbor ', '8083889629': 'Dr. Effiong Okon Ekaeba', '8062279615': 'Dr. John Oladejo', '+234810739-2731': 'Dr Oluchi John-Isiodu', '2347034054962': 'Adeniyi Salaudeen', '+234 (9) 4615700': 'Amin Abubakar Sadiq ', ' +2348023935869': 'Amin Abubakar Sadiq ', '+234(0)80 9099 8811': 'Adaobi Ekweanya ', '803 309 5945': 'Helen Tamunoibelema ', '7038402601': 'ALEXANDER IFEANYI OGOLO', ' 08059453568': 'ALEXANDER IFEANYI OGOLO', '802 324 5490': 'Debbie Akwara', '8062625402': 'Maikudi Ibrahim Abubakar', '7030834395': 'Engr. Mahraz Karaye', '7068490339': 'Titilayo Wumi Oluwafemi', '8035136609': 'Stephen Bamidele Ogodo', ' 09098109072': 'Stephen Bamidele Ogodo', '8060740202': 'Dr. Alhaji Musa Liman', '7038080616': 'Lovelyn Okoye', '255627542057': 'Ernest Masasi', '2348033145174': 'Dominic Okafor ', '+447741368789 ': 'Salisu Uba ', '8189624547': 'Benson Ndaji ', ' 2348064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '+2348037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO,', '2347033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '+2348052362288': 'Moses Mogbolu ', ' +2348159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', '  +44 7512 093697': 'Ayodapo Oyebade ', ' +44 7824 798888': 'Ayodapo Oyebade ', ' +44 7043 050050': 'Ayodapo Oyebade ', '+234-1-4614016-7': 'Victoria Alonge ', ' 7359948': 'Victoria Alonge ', ' +2348023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', 'george.obi@singeobigroup.com': '"George Obi" ', '7031042122': 'Oyegoke Adekunle Alani', '8173015230': ' Akinlamilo Elliot Olafisoye', ' 08033015230': ' Akinlamilo Elliot Olafisoye', '+2438037012676': 'Oyinloye Oyedele P.', ' +2439029461146 ': 'Oyinloye Oyedele P.', '+256 417 201 019': 'Adekemi Ndieli ', ' +256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O', '8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '9037808592': 'Engr. Benjamin Eboehi', ' 08035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '8061296216': 'Godwin Okoko ', '8133943520': '"Oluwole Olukoya" ', '7032220542': 'PIUS IPUOLE ', '8032327228': 'Prof Samuel Ogunwale Ogundiran', ' 08030917088': 'Prof Samuel Ogunwale Ogundiran', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '234803 493 2689': 'LAWSON BEESON ', '+2347069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '2348032601105': 'Hon. Anselm C. Onuorah',  '8024260942': 'Gidado Tahir ', '8036469928': 'Mohammed Saeed Suleiman ', ' 08098469928': 'Mohammed Saeed Suleiman ', '8036754537': 'Ogechukwu Eucharia Maduka', '1. (+234) (1) 2954690 2': 'Adeyinka Adegbite, Esq', ' (+234) (1) 2954691 3': 'Adeyinka Adegbite, Esq', ' (+234)9053333393': 'Adeyinka Adegbite, Esq', '8056659371': 'Dr. Olotu, O. Ayopo', ' 08098929477': 'Dr. Olotu, O. Ayopo', '8062862692': 'Victor Bisong', '7084415597': 'Ismaila Haliru Zarma', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '8035995868': 'Hawa BenHirki ', '+234 (1) 2713990 ': 'Kayode Ibrahim AKINTOLU', ' +2348086633083': 'Kayode Ibrahim AKINTOLU', '+234 810 375 6894': 'Reginald Udenze Ihedike', '+2347039554117': ' Job Ayodele Ekundayo', '7060772784': 'Victor Obioma Uche', '8033865790': 'Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart ',  '8033778222': 'Frederick Bethel Saduwa ', '234 (0) 803 334 1079 ': 'Joseph Isere ', ' 07068600006 ': 'Kennedy Akpan', ' 09027936331': 'Kennedy Akpan', '2348056038074': 'ONABEKUN ADEKUNLE ', ' +234702540721': 'ONABEKUN ADEKUNLE ', ' +234-7037905644 ': 'Idornigie Ide Christopher ', ' 08071827748': 'Idornigie Ide Christopher ', '8038442908': 'Emmanuel Olawuyi ', ' +27 12 394 1158': 'Nthabiseng Maude Mthethwa(DBA)Hon.', ' +27 82 635 1627': 'Nthabiseng Maude Mthethwa(DBA)Hon.','8033815239': 'Chukwuka Egbule (M.Sc., FCA, FCTI)', ' 08058448143 ': 'Chukwuka Egbule (M.Sc., FCA, FCTI)', ' (234) 8052448149': 'JOSEPH HUMPHREY KABE', '8033509752': 'Idumonza Isidahomhen ', '+234-08052913643': 'Abimbola Omolabi PhD', ' +234-08033172828': 'Abimbola Omolabi PhD', '8094773839': 'Francois Hounda DOSSOU', '8037093585': 'Nkem Joseph-Palmer ', ' 09023924412': 'Nkem Joseph-Palmer ', ' 07046852104': 'Nkem Joseph-Palmer ', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7020677189': 'Ndubuwa Ugwunna Victor', '9087259465': 'Engr Jane Ifeoma Kamanya', '8144513831': 'Dr Muhammad Kabir Adam', ' 0708160': 'Dr Muhammad Kabir Adam', '+2348064657799': 'Dr Joseph Rankin', '+2348102875997': 'Dr Joseph Rankin', '8032479757': 'Aiyedun Olubunm Fcis Mtm', '712187260': 'Dr Kasozi Nathan', ' 0702916735': 'Dr Kasozi Nathan', '7035466027': 'Emmanuel Oladipo Akogun ', '8069317779': 'Titi Yakubu ', '8033156025 ': 'Engr Aishatu Aliyu Umar, FNSE', ' 08095000000': 'Engr Aishatu Aliyu Umar, FNSE', '8033107505': 'Mrs Juliet Ogedi David-west', '8065660093': 'Roselyn Eneji', '+234 803 4071 116': 'Paul Nnamah ', '8055076706': 'Olajide Ojo ', '904530629': 'Abayomi Bello', '8039689404': 'WILSON OBIDAH, PhD', '8033496839': 'Dr. Charles Anosike FCMI MNIM GPM', '8033613144': 'Ujunwa Rosemary Felicia (Mrs)', ' +2348055266838': 'Peter Imafidon Omokaro', '8062611560': 'Olusegun Adepoju', '2348032007440': 'Erere Oyibo-Rhokaye ', '+2348033467900': 'Dr. Chukwunonso Izuchukwu Pharm.d Cmc Fimc', '8033377261': 'Prof. Basil O. Nwosu', '8055928327': 'Rev. Sr. Paulette Ekejiuba Phd', '+2348037109285': 'Ndifreke Andrew-essien', '8033335091': 'Barr. Miss Chigozie Ifeoma Nwagbara', ' 07088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', ' 08156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8128678873': 'Mr. Aniefiok E. Thomas', '+23279881111\xa0 ': 'Dipo Gbenro ', '+23276368  359': 'Dipo Gbenro ', '+447443423890': 'Uchennia Akahalu ', '+2347067941550': 'Bldr. Alvary A. Durkwa', '8030717044': 'Derek Omoleh ', '8055427409': 'Uchenna A. Okoroafor', '8032195105': 'Dr. Victor Evans', '8056488800': 'Akinbebije Damilola', '8035983539': 'Shitery Aaron Istifanus', '8066789611': 'Leonard Nzenwa ', '8062411073': 'Sunday Bala ', '+2349036683244': 'Busari Matthew', ' +2348060895366': 'Busari Matthew', '7080858791': 'Uchenna Solomon Ohaeri ', '2349039231107': 'Joshua Samuel', '7011990709': 'Ogunbiyi-davies Biodun Abiola', '8051500690': ' Osinuga Rahman', '8111312517': 'Eluozo Collins ', '23408032825342': 'Engr Olatunde Micheal IBRAHIM', ' 08188541950': 'Engr Olatunde Micheal IBRAHIM', '8034531431': 'Olajire Adebayo Aderemi', '9097512017': 'Ashikia Festus Uwakhemen', '8163686103': 'Dr. Ola Adigun-Daniels', '8069680993': 'Orkuma Emmanuel Anyoko-Shaba', '8037829881': 'Maharaz Saad', '8027291738': 'CHRISTWEALTH Kolawole Olusola', '8036197738': 'Aromeh Sunday Adole', '8037262350': 'George Idiaghe', '8061572906': 'Uwem Mkpong  Archibong', '8033047278': 'Nasamu Ibrahim', '8034315211': 'Olatunde Sowunmi', '8033118894': ' Igenegbai Christiana Joy', '8035677488': 'Ekemezie Okechukwu '}
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

#check out zuhair, and shirley
#{   }



contacts=  {'8035028205': 'Akpe Oyinkarebai Michael', '7039094177': 'Chris Manuawuchukwu  Agu',  '+48572537567': ' Dr. James Onyinye Mbakpou', ' +48669784338': ' Dr. James Onyinye Mbakpou', ' +375299641852': ' Dr. James Onyinye Mbakpou', '8022226864': 'Onalu Uchenna . C\t\t', '8037003649': 'HASSAN SALIHU ANKA ', '\t7031384185': 'Adewale Davies Owoyemi\t', ' 08023012752': 'Adewale Davies Owoyemi\t', '8034746507': 'Barr Lohor Alexander\t\t', '8033483674': 'Essang Paddy\t', '7088607443': 'Prince Amaefula\t\t', '8080767155': 'Chukwudi Iwuozor\t\t', '8023608704': 'Patricia Eze', '8055613009': 'Folashade Olubukola Aderanti-Olowoshoke\t', '7035558287': 'Stephen Eche', '8131538812': 'SP Onyejegbu Basilia Cynthia\t', '8030824948': 'Ogunmefun Toyin\t', '8033341416': 'OLANIRAN ADERIBIGBE', '8033156117': 'Umar B. Bindir', '8173245448': 'Shirley Ehru Nehemiah', '8037879235': 'Dr ZUHAIR JIBIR ',  '7036481502': 'Eni Okoi, Esq', '8033078252': 'Peter Imafidon Omokaro', ' 8173078252': 'Peter Imafidon Omokaro', '8055266838': 'PETER OMOKARO MBA, FIMC,CMC,FCIB ', ' 8033886655 ': 'Seun Sodipe ', ' 8172925952': 'Seun Sodipe ', '8027862387': 'Austin Itsoya Momodu', '': 'Markus Njidda Uba ', ' (0)8028911399': 'Markus Njidda Uba ', '(0)8068056242': 'Markus Njidda Uba ', '8035881242': 'Emmanuel Akissa', '8032212135': 'Emumena, David Emuhowho', '7054069661': 'Daperi Amachree ', '8023361732': 'Prof. Kessington Obahiagbon', '8037010777': 'Rev. Jim Piomoki-Stevens', '(647) 203-0350': 'Prof. Adefemi Olokesusi (Ph.D)', '8037008618': 'KALU, Peters PhD', '+233 200 429 430': 'Kenneth Igiri ', ' +233 544 904 920': 'Kenneth Igiri ', '8033165162': 'Terseer Ugbor ', '8083889629': 'Dr. Effiong Okon Ekaeba', '8062279615': 'Dr. John Oladejo', '810739-2731': 'Dr Oluchi John-Isiodu', '7034054962': 'Adeniyi Salaudeen', ' (9) 4615700': 'Amin Abubakar Sadiq ', ' 8023935869': 'Amin Abubakar Sadiq ', '(0)80 9099 8811': 'Adaobi Ekweanya ', '803 309 5945': 'Helen Tamunoibelema ', '7038402601': 'ALEXANDER IFEANYI OGOLO', ' 08059453568': 'ALEXANDER IFEANYI OGOLO', '802 324 5490': 'Debbie Akwara', '8062625402': 'Maikudi Ibrahim Abubakar', '7030834395': 'Engr. Mahraz Karaye', '7068490339': 'Titilayo Wumi Oluwafemi', '8035136609': 'Stephen Bamidele Ogodo', ' 09098109072': 'Stephen Bamidele Ogodo', '8060740202': 'Dr. Alhaji Musa Liman', '7038080616': 'Lovelyn Okoye', '255627542057': 'Ernest Masasi', '8033145174': 'Dominic Okafor ', '+447741368789 ': 'Salisu Uba ', '8189624547': 'Benson Ndaji ', ' 8064710849': 'Benson Ndaji ', '8039098931': 'JAMES SONDE ', '8037257819': 'OSUJI ALBERTO OBINNA', '8037126431': 'Akachukwu Moses Chukwudi', '8023204661': 'AZUBUIKE CHIDOZIE OKONKWO,', '7033200500': 'Uko Ekott, (FCIA, DCILRM, FIMC, CMC)', '8052362288': 'Moses Mogbolu ', ' 8159552222': 'Moses Mogbolu ', '8166615002': 'IBRAHIM ABDULRASHEED OZOVEHE', '8167353993': 'Tope Oluwadare ', '  +44 7512 093697': 'Ayodapo Oyebade ', ' +44 7824 798888': 'Ayodapo Oyebade ', ' +44 7043 050050': 'Ayodapo Oyebade ','-1-4614016-7': 'Victoria Alonge ', ' 7359948': 'Victoria Alonge ', ' 8023231273 ': 'Victoria Alonge ', '8064499724': 'Mr. S. Kola Adekoya', 'george.obi@singeobigroup.com': '"George Obi" ', '7031042122': 'Oyegoke Adekunle Alani', '8173015230': ' Akinlamilo Elliot Olafisoye', ' 08033015230': ' Akinlamilo Elliot Olafisoye', '+2438037012676': 'Oyinloye Oyedele P.', ' +2439029461146 ': 'Oyinloye Oyedele P.', '+256 417 201 019': 'Adekemi Ndieli ', ' +256 771 003 594': 'Adekemi Ndieli ', '8033296209': 'Dr. Sylvester C. Offor FCA', '8033262326': 'Ezeogbuefi Gabriel .O', '8131634324': 'ISHOLA-COKER OLUWATOSIN', '8055128300': 'Abimbola Olulana', '9037808592': 'Engr. Benjamin Eboehi', ' 08035665315': 'Engr. Benjamin Eboehi', '8036342106': 'KASSIM IDRIS', '8061296216': 'Godwin Okoko ', '8133943520': '"Oluwole Olukoya" ', '7032220542': 'PIUS IPUOLE ', '8032327228': 'Prof Samuel Ogunwale Ogundiran', ' 08030917088': 'Prof Samuel Ogunwale Ogundiran', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM', '803 493 2689': 'LAWSON BEESON ', '7069551267': 'LAWSON BEESON ', '8035446978': 'Promise Nwafor A Anelechi ', '8032601105': 'Hon. Anselm C. Onuorah',  '8024260942': 'Gidado Tahir ', '8036469928': 'Mohammed Saeed Suleiman ', ' 08098469928': 'Mohammed Saeed Suleiman ', '8036754537': 'Ogechukwu Eucharia Maduka', '1. (+234) (1) 2954690 2': 'Adeyinka Adegbite, Esq', ' (+234) (1) 2954691 3': 'Adeyinka Adegbite, Esq', ' (+234)9053333393': 'Adeyinka Adegbite, Esq', '8056659371': 'Dr. Olotu, O. Ayopo', ' 08098929477': 'Dr. Olotu, O. Ayopo', '8062862692': 'Victor Bisong', '7084415597': 'Ismaila Haliru Zarma', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '8035995868': 'Hawa BenHirki ', ' (1) 2713990 ': 'Kayode Ibrahim AKINTOLU', ' 8086633083': 'Kayode Ibrahim AKINTOLU', ' 810 375 6894': 'Reginald Udenze Ihedike', '7039554117': ' Job Ayodele Ekundayo', '7060772784': 'Victor Obioma Uche', '8033865790': 'Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart ','8033778222': 'Frederick Bethel Saduwa ', ' (0) 803 334 1079 ': 'Joseph Isere ', ' 07068600006 ': 'Kennedy Akpan', ' 09027936331': 'Kennedy Akpan', '8056038074': 'ONABEKUN ADEKUNLE ', ' 702540721': 'ONABEKUN ADEKUNLE ', ' -7037905644 ': 'Idornigie Ide Christopher ', ' 08071827748': 'Idornigie Ide Christopher ', '8038442908': 'Emmanuel Olawuyi ', ' +27 12 394 1158': 'Nthabiseng Maude Mthethwa(DBA)Hon.', ' +27 82 635 1627': 'Nthabiseng Maude Mthethwa(DBA)Hon.',  '8033815239': 'Chukwuka Egbule (M.Sc., FCA, FCTI)', ' 08058448143 ': 'Chukwuka Egbule (M.Sc., FCA, FCTI)', ' () 8052448149': 'JOSEPH HUMPHREY KABE', '8033509752': 'Idumonza Isidahomhen ', '-08052913643': 'Abimbola Omolabi PhD',  '8094773839': 'Francois Hounda DOSSOU', '8037093585': 'Nkem Joseph-Palmer ', ' 09023924412': 'Nkem Joseph-Palmer ', ' 07046852104': 'Nkem Joseph-Palmer ', '+27216502049': 'Abimbola Windapo PhD, PrCPM, FNIOB', '7020677189': 'Ndubuwa Ugwunna Victor', '9087259465': 'Engr Jane Ifeoma Kamanya', '8144513831': 'Dr Muhammad Kabir Adam', ' 0708160': 'Dr Muhammad Kabir Adam', '8064657799': 'Dr Joseph Rankin', '8102875997': 'Dr Joseph Rankin', '8032479757': 'Aiyedun Olubunm Fcis Mtm', '712187260': 'Dr Kasozi Nathan', ' 0702916735': 'Dr Kasozi Nathan', '7035466027': 'Emmanuel Oladipo Akogun ', '8069317779': 'Titi Yakubu ', '8033156025 ': 'Engr Aishatu Aliyu Umar, FNSE', ' 08095000000': 'Engr Aishatu Aliyu Umar, FNSE', '8033107505': 'Mrs Juliet Ogedi David-west', '8065660093': 'Roselyn Eneji', ' 803 4071 116': 'Paul Nnamah ', '8055076706': 'Olajide Ojo ', '904530629': 'Abayomi Bello', '8039689404': 'WILSON OBIDAH, PhD', '8033496839': 'Dr. Charles Anosike FCMI MNIM GPM', '8033613144': 'Ujunwa Rosemary Felicia (Mrs)', ' 8055266838': 'Peter Imafidon Omokaro', '8062611560': 'Olusegun Adepoju', '8032007440': 'Erere Oyibo-Rhokaye ', '8033467900': 'Dr. Chukwunonso Izuchukwu Pharm.d Cmc Fimc', '8055928327': 'Rev. Sr. Paulette Ekejiuba Phd', '8037109285': 'Ndifreke Andrew-essien', '8033335091': 'Barr. Miss Chigozie Ifeoma Nwagbara', ' 07088932144': 'Barr. Miss Chigozie Ifeoma Nwagbara', ' 08156562674': 'Barr. Miss Chigozie Ifeoma Nwagbara', '8128678873': 'Mr. Aniefiok E. Thomas', '+23279881111\xa0 ': 'Dipo Gbenro ', '+23276368  359': 'Dipo Gbenro ', '+447443423890': 'Uchennia Akahalu ', '7067941550': 'Bldr. Alvary A. Durkwa', '8030717044': 'Derek Omoleh ', '8055427409': 'Uchenna A. Okoroafor', '8032195105': 'Dr. Victor Evans', '8056488800': 'Akinbebije Damilola', '8035983539': 'Shitery Aaron Istifanus', '8066789611': 'Leonard Nzenwa ', '8062411073': 'Sunday Bala ', '9036683244': 'Busari Matthew',  '7080858791': 'Uchenna Solomon Ohaeri ', '9039231107': 'Joshua Samuel', '7011990709': 'Ogunbiyi-davies Biodun Abiola', '8051500690': ' Osinuga Rahman', '8111312517': 'Eluozo Collins ', '08032825342': 'Engr Olatunde Micheal IBRAHIM', ' 08188541950': 'Engr Olatunde Micheal IBRAHIM', '8034531431': 'Olajire Adebayo Aderemi', '9097512017': 'Ashikia Festus Uwakhemen', '8163686103': 'Dr. Ola Adigun-Daniels', '8069680993': 'Orkuma Emmanuel Anyoko-Shaba', '8037829881': 'Maharaz Saad', '8027291738': 'CHRISTWEALTH Kolawole Olusola', '8036197738': 'Aromeh Sunday Adole', '8037262350': 'George Idiaghe', '8061572906': 'Uwem Mkpong  Archibong', '8033047278': 'Nasamu Ibrahim', '8034315211': 'Olatunde Sowunmi', '8067742773': 'Mr. Awusa Peter Ewa',  '8067742773': 'Mr. Awusa Peter Ewa','8033118894': ' Igenegbai Christiana Joy', '8035677488': 'Ekemezie Okechukwu '}
older = { '8036197738': 'Aromeh Sunday Adole', '8027291738': 'Christwealth Kolawole','8037829881': 'Maharaz Saad', '8069680993': 'Orkuma Anyoko - Shaba', '8039689404': 'Wilson Obidah, PhD', '8035672752': 'Victoria', '9036683244': 'Musari Mathew', '8060895366': 'Musari Mathew', '8032825342': 'Engr.Olatunde Michael Ibrahim', '8188541950': 'Engr.Olatunde Michael Ibrahim', '8051500690': 'Osinuga Rahman', '8062411073': 'Bala, Sunday', '8066789611': 'Leonard Nzenwa', '8032195105': 'Dr.Victor Evans.', '8058434421': 'Jatto Osabuhen Jonathan', '8056488800': 'Akinbebije Damilola', '8033597679': 'Mr. Adigun Oluwamayowa Oluwaseun Kingsley', '8035881242': 'Emmanuel Akissa',  '8023152210': 'Oke Olabamiji', '8036206061': ' Oke Olabamiji', '8033015230': ' AKINLAMILO, ELLIOT OLAFISOYE',  '8037257819': 'OSUJI ALBERTO OBINNA', '8035983539': 'Shitery Aaron Istifanus', '8035691309': 'Olusegun Adepoju', '8033496839': 'Dr. Charles Anosike FCMI, MNIM GPM', '8032007440': 'Mr.Erere Oyibo - Rhokaye', '8032479757': 'Aiyedun Olubunm FCIS, MTM','8036469928': 'Mohammed Saeed Suleiman', '8068056242': 'Markus Njidda Uba', '8055928327': 'Rev. Sr. Paulette Ekejiuba, PhD', '8144513831': 'Comrade DR Mk Adam Rano (Dr Muhammad Kabir Adam)', '8086633083': 'Kayode Akintolu', '8037093585': 'Nkem Joseph-Palmer', '9023924412': 'Nkem Joseph-Palmer', '8023204138': 'Elvis Onuora FCA, FCTI', '8052913643': 'Abimbola Omolabi PhD', '8033172828': 'Abimbola Omolabi PhD', '8052448149': 'JOSEPH HUMPHREY KABE', '7039554117': 'Job Ayodele Ekundayo', '8033865790': 'Prof. Sulaiman Olanrewaju Adebayo', '8033448986': 'Frederick Hart', '8036005365': 'Muhammad Kachallah', '8033778222': 'Frederick Bethel Saduwa', '8033341079': 'ISERE Joseph', '8173245448': 'Shirley Ehru Nehemiah', '8033266113': 'OLUWAMODUPE NDIDIAMAKA OGUNBANJO', '7084415597': 'Ismaila Haliru Zarma', '906 639 2092': 'Rev. Sr. Dr. Antoinette Nneka Opara', '7036481502': 'Eni Okoi, Esq.',  '8032601105': 'Hon. Anselm C. Onuorah', '7069551267': 'Beeson Lawson', '8022230635': 'Engr. Jatto Abulkareem , FNSE, FNIEEE,FNIPE, FIMC, FOSHAuk, FNIM',   '7032220542': 'PIUS IPUOLE', '8033341416': 'OLANIRAN ADERIBIGBE', '8036754537': 'Ogechukwu Eucharia Maduka', '8062862692': 'Victor Bisong',}
#
def gjiof():
    for old in older.keys():
        try:
            check = contacts[old]
        except:
            print(old, older[old], 'not found')
