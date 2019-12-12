# coding:utf-8
import pymysql


class OperationMysql:
    '''
    封装数据库操作
    '''

    def __init__(self):
        '''
        初始连接数据库, 此数据库部署在测试环境A
        '''
        self.conn = pymysql.connect(
            host='10.1.200.166',
            port=3306,
            user='lagourw',
            passwd='JUY#*f2349Kl',
            db='lagou_resume',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def get_db_data(self, phone):
        '''
        根据caseid找到对应用例内容
        :param case_id: str
        :return: dict
        '''
        case_data = self.search_one("SELECT * FROM r_resume where %s " % phone)
        return case_data

    def search_one(self, sql):
        '''
        执行SQL语句, 返回一条结果, 再次执行返回下一个结果
        :param sql: str, sql语句
        :return: dict
        '''
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

    def search_all(self, sql):
        '''
        执行SQL语句, 获取全部数据
        :param sql: str, sql语句
        :return: dict
        '''
        self.conn.ping(reconnect=True)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def update_all(self, sql):
        try:
            self.conn.ping(reconnect=True)
            effect_row = self.cur.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            print(e)
            effect_row = 0
            self.conn.rollback()
        return effect_row


# if __name__ == '__main__':
#     op_mysql = OperationMysql()
#     #     # res = op_mysql.get_db_data(13300000011)
#     #     # args={'userid':537}
#     #     # res = op_mysql.search_one("SELECT id FROM r_resume where userId = %d " % args['userid'])
#     #     res = op_mysql.update_all('UPDATE r_resume set sex = "男" WHERE id = 1')
#     args = {"id": 156, "name": "桃花源", "sex": "男", "birthday": "1990.09", "email": "tester2018@sina.com",
#             "liveCity": "北京", "work_year": "7年", "joinWorkTime": "2013.07", "companyName": "拉勾网4324",
#             "department": "用户价值部", "positionNameType1": "开发|测试|运维类", "positionNameType2": "后端开发",
#             "positionType": "Python", "positionName": "Python", "startDate": "2018.07", "endDate": "至今",
#             "companyIndustry": "新零售", "skillLabel": ['后端', '服务器端', '客户端'],
#             "workContent": "<p>我任职XX公司XX部门，该部门后台系统主要由API模块，APP后台模块，算法模块以及数据模块组成。后台的所有任务通过分布式任务系统进行任务管理。整套系统部署在公司的私有服务器上，主要基于公司的Mysql集群和Redis集群做数据存储，使用MQ集群做消息队列，基于ZK集群搭建高可用系统，前期我们服务之前的调用方式都是基于HTTP的方式，服务耦合性较高，后期我们基于Motan框架做了整个系统的微服务化。<br /></p>",
#             "schoolName": "北京理工大学", "professional": "计算机科学与技术", "ed_startDate": "2009", "ed_endDate": "2012",
#             "education": "硕士", "ex_positionName": "t", "ex_positionType": "全职", "salarys": "10k-15k", "city": " 上海",
#             "status": "随便看看", "arrivalTime": "2周-1个月", "label_name": "演讲能力",
#             "myRemark": "<p>行我可以我最棒我最好我能行我可以我最棒我最好我能行我可以我最棒我最好<br /></p><p><br /></p>"}

    # res = op_mysql.update_all(
    #     "UPDATE r_resume SET name = %s,sex = %s, birthday = %s, email= %s , liveCity= %s, work_year= %s, joinWorkTime = %s WHERE id = 156" %
    #     args['name'], args['sex'], args['birthday'], args['email'], args['liveCity'], args['work_year'],
    #     args['joinWorkTime'])

    # res = op_mysql.update_all(
    #     "UPDATE r_resume SET name = '%s',sex = '%s', birthday = '%s', email= '%s' , liveCity= '%s', work_year= '%s', joinWorkTime = '%s' WHERE id = %d" % (
    #         args['name'], args['sex'], args['birthday'], args['email'], args['liveCity'], args['work_year'],
    #         args['joinWorkTime'], int(args['id']))
    # )
    # r_expect_jobs_effect_row = op_mysql.update_all(
    #     "UPDATE r_expect_jobs SET positionName = '%s',positionNameType1 = '%s',positionNameType2='%s',positionType='%s',salarys='%s',city='%s',status='%s',arrivalTime='%s' WHERE resumeId = %d" % (
    #         args['ex_positionName'], args['positionNameType1'], args['positionNameType2'], args['ex_positionType'],
    #         args['salarys'], args['city'],
    #         args['status'], args['arrivalTime'], args['id']))
    # print(r_expect_jobs_effect_row)
