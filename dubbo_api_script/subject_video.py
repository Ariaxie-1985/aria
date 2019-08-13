# coding:utf-8
# @Time  : 2019-08-02 17:48
# @Author: Xiawang
import json
import time

import pymysql

from utils.telnet_invoke_dubbo import Dubbo
from faker import Faker

conn = Dubbo('10.1.201.238', 30060)

fake = Faker("zh_CN")


def post_teamstory_case(data):
    '''
        新建团队故事, 打印故事id, 详见库表lagou.company_team_story
    '''
    teamstory_service_name = 'com.lagou.service.business.base.company.api.CompanyTeamStoryRemoteService'
    teamstory_method_name = 'add'
    result = conn.invoke(
        teamstory_service_name,
        teamstory_method_name,
        data
    )
    print(result)


def post_video_case(data):
    '''
    新建视频, 打印视频id, 详见库表lagou.company_video
    '''
    video_service_name = 'com.lagou.service.business.base.company.api.CompanyVideoRemoteService'
    video_method_name = 'addVideo'
    result = conn.invoke(
        video_service_name,
        video_method_name,
        data
    )
    print(result)


def post_subject_case(data):
    '''
    新建专题, 打印专题id, 详见库表 lagou.company_video_subject_dictionary
    其中sorted要唯一
    '''
    subject_service_name = 'com.lagou.service.business.base.company.api.CompanySubjectDictionaryRemoteService'
    subject_method_name = 'saveOrUpdate'
    result = conn.invoke(
        subject_service_name,
        subject_method_name,
        data
    )
    print(result)


def post_subjecy_video_case(data):
    '''
    将专题和视频关联起来 详见库表lagou.company_video_subject
    依赖专题id, 视频id, 其中sorted要唯一
    '''
    subject_video_service_name = 'com.lagou.service.business.base.company.api.CompanySubjectVideoRemoteService'
    subject_video_method_name = 'saveOrUpdate'
    result = conn.invoke(
        subject_video_service_name,
        subject_video_method_name,
        data
    )
    print(result)


def insert_video_spot(company_id, company_video_id, url, spot_time, content):
    def connect_db():
        db = pymysql.connect(
            host='10.1.200.166',
            port=3306,
            user='lagourw',
            passwd='JUY#*f2349Kl',
            db='lagou',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = db.cursor()
        return db, cursor

    db, cursor = connect_db()
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql = "insert into company_video_bright_spot(company_id,company_video_id,url,time,content,create_time,is_del) VALUES({company_id},{company_video_id},'{url}',{spot_time},'{content}','{create_time}',0)".format(
        company_id=company_id, company_video_id=company_video_id, url=url, spot_time=spot_time, content=content,
        create_time=create_time)
    count = cursor.execute(sql)
    if count == 1:
        db.commit()
        print("添加视频亮点数据成功")
    else:
        print("添加视频亮点数据失败,请重试")


def queryWithChild_case(data):
    '''
    新建专题, 打印专题id, 详见库表 lagou.company_video_subject_dictionary
    其中sorted要唯一
    '''
    subject_service_name = 'com.lagou.service.business.base.company.api.CompanyVideoRemoteService'
    subject_method_name = 'queryWithChild'
    result = conn.invoke(
        subject_service_name,
        subject_method_name,
        data
    )
    print(result)


def addVideoQuestions_case(data):
    '''
    新建专题, 打印专题id, 详见库表 lagou.company_video_subject_dictionary
    其中sorted要唯一
    '''
    subject_service_name = 'com.lagou.service.business.base.company.api.CompanyVideoRemoteService'
    subject_method_name = 'addVideoQuestions'
    result = conn.invoke(
        subject_service_name,
        subject_method_name,
        data
    )
    print(result)


if __name__ == '__main__':
    options = ["八月","九月","六月"]
    options = json.dumps(options).replace('"', '\\"')
    data = [{"companyId": 142136, "companyVideoId": 98, "question": "黑衣人什么时候上映?", "options": options, "rightAnswers": "六月"}]
    addVideoQuestions_case(data)
    # queryWithChild_data = (142136, "CREATE_TIME_DESC")
    # queryWithChild_case(queryWithChild_data)

    teamstory_data = {'companyId': 142136, 'title': '燃烧我的卡路里', 'publisherName': '杨超越',
                      'publisherPortrait': 'http://www.lgstatic.com/i/audio1/M00/01/C1/CgHIk1wKHMCAaRmJAADz0rn5NFQ998.jpg',
                      'publisherPosition': '歌手'}
    # post_teamstory_case(teamstory_data)

    url_list = ["http://vfx.mtime.cn/Video/2019/06/12/mp4/190612205428644400.mp4",
                "http://vfx.mtime.cn/Video/2019/06/11/mp4/190611221730282660.mp4",
                "http://vfx.mtime.cn/Video/2019/06/11/mp4/190611000340681831.mp4",
                "http://vfx.mtime.cn/Video/2019/06/10/mp4/190610141939766739.mp4",
                "http://vfx.mtime.cn/Video/2019/06/05/mp4/190605185204356232.mp4",
                "http://vfx.mtime.cn/Video/2019/06/05/mp4/190605101703931259.mp4"]
    description_list = ["中国科幻《上海堡垒》新预告外星母舰入侵", "魔幻再起！《冰雪奇缘2》曝正式预告", "不是喜剧！邓超导演《银河补习班》发新预告",
                        "彭昱畅侯明昊《回到过去拥抱你》预告", "布拉德皮特科幻新作《星际探索》预告", "《黑衣人：全球追缉》星际对决终极预告"]
    coverUrl_list = ["http://img5.mtime.cn/mg/2019/06/12/205329.35792320_120X90X4.jpg",
                     "http://img5.mtime.cn/mg/2019/06/11/202131.80341046_120X90X4.jpg",
                     "http://img5.mtime.cn/mg/2019/06/11/000307.58997745_120X90X4.jpg",
                     "http://img5.mtime.cn/mg/2019/06/10/141934.94618257_120X90X4.jpg",
                     "http://img5.mtime.cn/mg/2019/06/05/165003.81721110_120X90X4.jpg",
                     "http://img5.mtime.cn/mg/2019/06/05/101656.54539982_120X90X4.jpg"]
    duration_list = [79, 79, 121, 73, 152, 96]
    title_list = ["上海堡垒 正式版预告片", "冰雪奇缘2 正式中文预告", "银河补习班 剧场版预告片", "回到过去拥抱你 先导预告", "星际探索 台版中字预告", "黑衣人：全球追缉 星际对决终极预告"]
    # for i in range(0, 6):
    #     parent_video_data = {"companyId": 142136, "storyId": 18,
    #                          "url": url_list[i], 'description': description_list[i],
    #                          "coverUrl": coverUrl_list[i],
    #                          "size": '23.01',
    #                          "duration": duration_list[i], "title": title_list[i]}
    #     post_video_case(parent_video_data)

    video_data = {"companyId": 142136, "storyId": 18,
                  "url": 'http://vfx.mtime.cn/Video/2019/06/18/mp4/190618080431698491.mp4',
                  'description': '人民解放军',
                  "coverUrl": 'http://img5.mtime.cn/mg/2019/06/18/080407.34376988_120X90X4.jpg', "size": '23.01',
                  "duration": 208, "title": "网游之黑袍纠察队", 'children': [{"companyId": 142136, "storyId": 18,
                                                                      "url": 'http://vfx.mtime.cn/Video/2019/06/18/mp4/190618083737248033.mp4',
                                                                      'description': '网游改编冒险电影《征途》定档预告',
                                                                      "coverUrl": 'http://img5.mtime.cn/mg/2019/06/18/083638.79639825_120X90X4.jpg',
                                                                      "size": '13.01', "duration": 56,
                                                                      "title": "征途 先导预告"}]}

    subject_data = {'name': '电影预告', 'style': '1', 'sorted': 24}
    # post_subject_case(subject_data)

    companyVideoId_list = [93, 94, 95, 96, 97, 98]
    # for i in range(0, 6):
    #     subject_video_data = {'companyId': 142136, 'companyVideoId': companyVideoId_list[i], 'videoSubjectId': 24,
    #                           'sorted': 11 + i}
    #     post_subjecy_video_case(subject_video_data)

    # insert_video_spot(company_id=142136, company_video_id=76, url="http://img5.mtime.cn/mg/2019/06/27/231348.59732586_120X90X4.jpg", spot_time=23, content="帅炸了！碉堡了！无与伦比！")
