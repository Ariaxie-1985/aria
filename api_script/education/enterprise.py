import json
import requests
from utils.util import login_password, get_requests
def enterprise_login():
    login_password('13252477137', '990eb670f81e82f546cfaaae1587279a')
    url = 'https://passport.lagou.com/ajaxLogin/frameGrant.html?fl=2&service=https%3A%2F%2Fkaiwu.lagou.com%2Fenterprise%2Findex.html%23%2Findex&osc=PASSPORT._pscb(1)&ofc=PASSPORT._pfcb(1)&pfurl=https%3A%2F%2Fkaiwu.lagou.com%2Fenterprise%2Findex.html%23%2Findex'
    get_requests(url, headers={'referer': 'https://kaiwu.lagou.com/enterprise/index.html'})
    search_referer_url = 'https://kaiwu.lagou.com/enterprise/index.html'
    get_requests(search_referer_url)

def search_staff():
    search_referer_url = 'https://kaiwu.lagou.com/enterprise/index.html'
    get_requests(search_referer_url)
    search_url = 'https://gate.lagou.com/v1/neirong/edu/enterprise/getStaffsByStudyState?studyState=STUDY&phone=&name=bj&pageNo=1&pageSize=20&enterpriseId=441'
    response = get_requests(url = search_url, headers={'x-l-req-header':'{deviceType:1}'})
    return response

if __name__ == '__main__':
    x = enterprise_login()
    p = search_staff()
    print(p)