import json
import requests
from utils.util import login_password, get_requests
def search_staff():
    search_referer_url = 'https://kaiwu.lagou.com/enterprise/index.html'
    get_requests(search_referer_url)
    search_url = 'https://gate.lagou.com/v1/neirong/edu/enterprise/getStaffsByStudyState?studyState=STUDY&phone=&name=bj&pageNo=1&pageSize=20&enterpriseId=2'
    response = get_requests(url = search_url, headers={'x-l-req-header':'{deviceType:1}'})
    return response
