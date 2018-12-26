#2018秋版合同刷新职位
from api_script.util import login ,get_code_token

login('00852','20181205')
def Refreshed():
    '''
    18版合同“刷新职位”
    :return:
    '''
    recruiter_reflash="https://easy.lagou.com/position/multiChannel/myOnlinePositions.htm?pageNo=1"
    queryAcount_header = get_code_token(recruiter_reflash)
    r = form_post(queryAcount_url, queryAcount_data, queryAcount_header)
    return r['content']['data']['data'][0]['userid']