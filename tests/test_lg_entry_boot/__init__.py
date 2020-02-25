# coding:utf-8
# @Time  : 2020/2/11 16:00
# @Author: Xiawang
# Description:
# import time
#
# from utils.util import get_requests
#
# url = 'https://www.zhipin.com/gongsi/?ka=header_brand'
# header = {
#     ':method': 'GET',
#     ':authority': 'www.zhipin.com',
#     ':path': '/gongsi/?ka=header_brand',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
#     ':scheme': 'https',
#     'sec-fetch-mode': 'navigate',
#     'accept-encoding': 'gzip, deflate, br',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': 1,
#     'pragma': 'no-cache',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
#     'cookie': '_uab_collina=158202124290316434873795; __c=1582021242; __g=-; __l=l=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DmeG7UTKjiW8HPgulum4fX0%252BgknuSTnZD8Z9EUgErSQg%253D%26name%3Dd8f4a6db%26ts%3D1582021380409%26callbackUrl%3D%252Fgongsi%252F%253Fka%253Dheader_brand%26srcReferer%3D&r=&friend_source=0&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a={}; lastCity=101010100; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a={time_stamp}; t=sPPTudS8MhnonLch; wt=sPPTudS8MhnonLch; __a=17725703.1582021242..1582021242.52.1.52.52; _bl_uid=tnky168gs2jrpOl0mw9kqk1bFUe5; __zp_stoken__=5bbdXyn47%2B%2BO6rB2HaowpK%2BkPsmMU%2FE%2Bpie1KhJhRNNDO7V9MZGLZbw1pHQ9pd1gmviPNtSh5Cza875erUWj2nXazFGz1gkSJuJ6LBxqHI3kAWs5TLUuQwuZ3BGE29%2BayuWF',
#     'referer': 'https://www.zhipin.com/web/common/security-check.html?seed=meG7UTKjiW8HPgulum4fX0%2BgknuSTnZD8Z9EUgErSQg%3D&name=d8f4a6db&ts=1582021380409&callbackUrl=%2Fgongsi%2F%3Fka%3Dheader_brand&srcReferer='
# }
# r = get_requests(url=url, headers=header, remark='fsd')
# print(r)
#
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "none"
# driver = webdriver.Chrome(executable_path='/opt/webdriver/bin/chromedriver')
#
# driver.get(url='https://www.zhipin.com')
#
# driver.add_cookie({'name': '_uab_collina', 'value': '158202124290316434873795'})
# driver.add_cookie({'name': '__c', 'value': '1582021242'})
# driver.add_cookie({'name': '__g', 'value': '-'})
# driver.add_cookie({'name': '__l',
#                    'value': 'l=https://www.zhipin.com/web/common/security-check.html?seed=meG7UTKjiW8HPgulum4fX0 gknuSTnZD8Z9EUgErSQg=&name=d8f4a6db&ts=1582021380409&callbackUrl=/gongsi/?ka=header_brand&srcReferer=&r=&friend_source=0&friend_source=0'})
# driver.add_cookie({'name': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a', 'value': '1582084278'})
# driver.add_cookie({'name': 'lastCity', 'value': '101010100'})
# driver.add_cookie({'name': '_bl_uid', 'value': 'tnky168gs2jrpOl0mw9kqk1bFUe5'})
# driver.add_cookie({'name': '_a', 'value': '17725703.1582021242..1582021242.65.1.65.65'})
# driver.add_cookie({'name': 'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a', 'value': '1582084278'})
# driver.add_cookie({'name': '__zp_stoken__',
#                    'value': '5bbdXyn47%2B%2BO6rB2HaowpK%2BkPj%2FtntvQvISDwkdaSzWl3U5CzB257m%2BbyPeyCgTIIXV5NtSh5Cza875erUWj2nXazAdMqFdhsnkA1NQ2a9r5Y0I5TLUuQwuZ3BGE29%2BayuWF'})
# driver.get(url='https://www.zhipin.com/gongsi/?ka=header_brand')
# company = driver.find_element_by_class_name('company-tab-box company-list')
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located(company))
# driver.quit()
