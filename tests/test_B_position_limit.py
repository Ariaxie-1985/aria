# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import logging
from api_script.business.B_position_limit import position_limit,getrefreshpoint,getpositionlimit,getonlinepositionlimit,isprivilige,offineposition
from util.util import login,assert_equal

login('00853','05180001')


def _position_limit():
    logging.getLogger().setLevel(logging.INFO)
    if isprivilige() == True:
        a,b = getpositionlimit()
        s,d,id = position_limit()
        success_message = '特权职位限制正确,'+'已发职位：'+str(d)+'.特权职位上限：'+str(a)+'.执行本用例前已存在的职位：'+str(b)
        fail_message = '特权职位限制异常或发布职位错误'+str(s)
        assert_equal(a-b,d,success_message,fail_message)
        '''
        try:
            assert a-b==d

            logging.info('职位限制正确,'+'已发职位：'+str(d)+'.特权职位上限：'+str(a)+'.执行本用例前已存在的职位：'+str(b))
        except:
            logging.info('职位限制异常或发布职位错误'+str(s))
        '''
    elif isprivilige() == False:
        onlinePosition, onlineLimitNum, createPositionNum, createLimitNum = getonlinepositionlimit()
        rfpoint = getrefreshpoint()
        # 刷新点数
        if (onlinePosition <= onlineLimitNum and createPositionNum <= createLimitNum) and rfpoint < 5:
            # 发布职位和在线职位均小于上限，刷新点数小于5
            if onlineLimitNum - onlinePosition <= createLimitNum - createPositionNum:
                # 可在线的职位数小于可发布的职位数，此时职位限制取在线职位
                s, i, id = position_limit()
                # i为本次发布的职位数
                success_message = '刷新点数小于5,在线职位达到上限时职位限制正确，已发布职位'+str(i)+'允许在线的职位数'+str(onlineLimitNum - onlinePosition)
                fail_message = '刷新点数小于5,在线职位达到上限时职位限制异常，已发布职位'+str(i)+'允许在线的职位数'+str(onlineLimitNum - onlinePosition)
                assert_equal(i,onlineLimitNum - onlinePosition,success_message,fail_message)
                # assert i == onlineLimitNum - onlinePosition
                # assert s['message'] == '职位点数不足，不能再发布'
            else:
                # 可在线的职位数大于可发布的职位数，此时职位限制取发布职位
                s, i, id = position_limit()
                fail_message = '刷新点数小于5,发布职位达到上限时职位限制异常，已发布职位'+str(i)+'允许发布的职位数'+str(createLimitNum - createPositionNum)
                success_message = '刷新点数小于5,发布职位达到上限时职位限制正确，已发布职位'+str(i)+'允许发布的职位数'+str(createLimitNum - createPositionNum)
                # assert i == createLimitNum - createPositionNum
                assert_equal(i,createLimitNum - createPositionNum,success_message,fail_message)
        elif (onlinePosition <= onlineLimitNum and createPositionNum <= createLimitNum) and rfpoint > 5:
            # 发布职位和在线职位均小于上限，刷新点数大于5
            if onlineLimitNum - onlinePosition <= createLimitNum - createPositionNum:

                # 可在线的职位数小于可发布的职位数，此时职位限制取在线职位
                a = onlineLimitNum - onlinePosition
                # 可免费发布的职位
                s, i, id = position_limit()
                # 发布职位直到不可发布为止
                rfposition = i - a
                # 使用刷新点数的职位，本次发布的所有职位减去免费发布的职位
                finalrfpoint = getrefreshpoint()
                # 使用后剩下的刷新点数
                fail_message = '刷新点数大于5，在线职位达到上限时职位限制异常，已发布付费职位'+str(rfposition)+'总发布职位数'+str(i)
                success_message = '刷新点数大于5，在线职位达到上限时职位限制正确，已发布付费职位'+str(rfposition)+'总发布职位数'+str(i)
                assert_equal(rfpoint - finalrfpoint,rfposition * 5,success_message,fail_message)
                # 判断已用刷新点数（初始的减最终的）与付费职位x5是否一样
                # assert rfpoint - finalrfpoint == rfposition * 5
            else:
                # 可在线的职位数大于可发布的职位数，此时职位限制取发布职位
                a = createLimitNum - createPositionNum
                s, i, id = position_limit()
                rfposition = i - a
                finalrfpoint = getrefreshpoint()
                fail_message = '刷新点数大于5，发布职位达到上限时职位限制异常，已发布付费职位' + str(rfposition) + '总发布职位数' + str(i)
                success_message = '刷新点数大于5，发布职位达到上限时职位限制正确，已发布付费职位' + str(rfposition) + '总发布职位数' + str(i)
                assert_equal(rfpoint - finalrfpoint,rfposition * 5,success_message,fail_message)
                # assert rfpoint - finalrfpoint == rfposition * 5
        elif (onlinePosition > onlineLimitNum or createPositionNum > createLimitNum) and rfpoint > 5:
            # 在线职位数大于在线职位限制或发布职位大于限制其刷新数大于5
            s, i, id = position_limit()
            fail_message = '刷新点数大于5，发布或在线职位超过上限，职位限制异常，发布职位数'+str(i)+'付费职位'+str(rfpoint // 5)
            success_message = '刷新点数大于5，发布或在线职位超过上限，职位限制正确，发布职位数'+str(i)+'付费职位'+str(rfpoint // 5)
            assert_equal(i,rfpoint // 5,success_message,fail_message)
            # 判断已发布的职位数，与刷新点数除以5（向下取整）是否相同
            # assert i == rfpoint // 5
        elif (onlinePosition > onlineLimitNum or createPositionNum > createLimitNum) and rfpoint < 5 :
            # 在线职位数大于在线职位限制或发布职位大于限制其刷新数小于5
            s, i, id = position_limit()
            fail_message ='刷新点数小于5，发布或在线职位超过上限，职位限制异常'+str(s)
            success_message ='刷新点数小于5，发布或在线职位超过上限，职位限制正常'+str(s)
            assert_equal(s['message'],'职位点数不足,不能再发布',success_message,fail_message)
    return id

# 执行次函数，包含自动下线已发职位
def test_position_limit_main():
    logging.getLogger().setLevel(logging.INFO)
    id = _position_limit()
    for i in id:
        try:
            s=offineposition(i)
        except:
            logging.info('职位下线失败'+str(s))
        else:
            logging.info('职位下线成功')



# print(test_position_limit())
# test_position_limit_main()
# print(39>5 or 65>10000 and 1>5)

