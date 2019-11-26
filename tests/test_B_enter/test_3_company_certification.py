from api_script.jianzhao_web.b_basic.toB_comleteInfo_3 import company_auth, completeInfo
from utils.util import login

def test_company_certification():
    company_auth()
    completeInfo()

if __name__ == '__main__':
    login('00852', '24482062')
    test_company_certification()
