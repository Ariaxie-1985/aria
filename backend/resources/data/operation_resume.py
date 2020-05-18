# coding:utf-8
# @Time  : 2019-04-02 11:29
# @Author: Xiawang
import time

from flask_restful import Resource, reqparse

# from backend.OperationMysql import OperationMysql

# op_mysql = OperationMysql()


class getResume(Resource):
    """ 查询及修改简历信息 """

    def get(self):
        """查询简历信息
                @@@
                ### Author = Xiawang

                ### Request Header
                | 字段 | 值 |
                | ---- | ---- |
                | method | GET |
                | content-type | application/json |


                ### 参数

                | 字段 | 类型 | 描述|
                | ---- | ---- | ---- |
                | phone | string | 用户手机号，非0086地区编号的手机号填写格式：地区编号+手机号 |
                | phone | string | 用户id  |



                ### 请求示例--直接在浏览器请求访问
                ```json
                http://127.0.0.1:9004//customer/resumedata?phone=0085220181208

                http://127.0.0.1:9004/customer/resumedata?userid=540

                ```

                ### 返回
                 ```json
                    {
	"state": 1,
	"content": "操作成功！",
	"result": {
		"basicMain": {
			"id": 156,
			"sex": "男",
			"birthday": "1990.09",
			"work_year": "7年",
			"phone": "0085220181208",
			"email": "tester2018@sina.com",
			"status": "我目前已离职，可快速到岗",
			"resumeName": "小宸的简历",
			"name": "桃花源55555",
		},
		"workExperience": {
			"id": 30,
			"companyName": "拉勾网",
			"positionName": "Python",
			"startDate": "2018.07",
		},
		"educationExperience": {
			"id": 156,
			"schoolName": "北京理工大学",
			"education": "硕士",
			"professional": "计算机科学与技术",
		},
		"ability_label": [{
			"create_time": "2019-04-03 18:56:48",
			"resume_id": 156,
			"name": "演讲能力",
			"is_del": 0,
			"update_time": "None"
		}],
		"expect_jobs": {
			"id": 156,
			"city": "上海",
			"positionType": "全职",
			"positionName": "Python",
			"salarys": "10k-15k",
			"isDel": 0,
			"positionNameType2": "后端开发",
			"arrivalTime": "2周-1个月",
			"positionNameType1": "开发|测试|运维类",
			"status": "随便看看"
		}
	}
}

                ```
                """
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, help="请输入正确手机号")
        parser.add_argument('userid', type=str, help="请输入正确userid")
        args = parser.parse_args()
        # if args['phone']:
        #     try:
        #         resume_id = op_mysql.search_one("SELECT id FROM r_resume WHERE phone = '%s'" % args['phone'])
        #         state = 1
        #         info = resume_id
        #         global resumeid
        #         resumeid = resume_id['id']
        #     except BaseException:
        #         state = 400
        #         info = "找不到简历id, 请确认下手机号填写是否正确"
        # elif args['userid']:
        #     try:
        #         resume_id = op_mysql.search_one(
        #             "SELECT id FROM r_resume WHERE userId = %d" % int(
        #                 args['userid']))
        #         state = 1
        #         info = resume_id
        #         resumeid = resume_id['id']
        #     except BaseException:
        #         state = 400
        #         info = "找不到简历id, 请确认下userid填写是否正确"
        # else:
        #     return {'state':400, 'content':'找不到简历id, 请确认下手机号、userid填写是否正确'}
        #
        # try:
        #     basicMain = op_mysql.search_one("SELECT * FROM r_resume WHERE id = '%s'" % resumeid)
        #     basicMain['createTime'] = str(basicMain['createTime'])
        #     basicMain['updateTime'] = str(
        #         basicMain.get('updateTime', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        #     workExperience = op_mysql.search_one(
        #         "SELECT * FROM r_work_experience WHERE resumeId = '%s' AND isDel = 0 ORDER BY createTime desc" % resumeid)
        #     if not (workExperience == None):
        #         workExperience['createTime'] = str(workExperience['createTime'])
        #
        #     educationExperience = op_mysql.search_one(
        #         "SELECT * FROM r_education_experience WHERE resumeId = '%s' AND isDel = 0 ORDER BY createDate desc" %
        #         resumeid)
        #     if not (educationExperience == None):
        #         educationExperience['createDate'] = str(educationExperience['createDate'])
        #
        #     ability_label = op_mysql.search_all(
        #         "SELECT * FROM r_ability_label WHERE resume_id = '%s' AND is_del = 0" %
        #         resumeid)
        #     if not (ability_label == None):
        #         for ab_label in ability_label:
        #             ab_label['create_time'] = str(ab_label['create_time'])
        #             ab_label['update_time'] = str(
        #                 ab_label.get('update_time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        #
        #     r_expect_jobs = op_mysql.search_one(
        #         "SELECT * FROM r_expect_jobs where resumeId = '%s'" %
        #         resumeid)
        #     r_expect_jobs['createTime'] = str(basicMain['createTime'])
        #     r_expect_jobs['updateTime'] = str(
        #         basicMain.get('updateTime', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        #     info = "操作成功！"

        # except:
        #     return {'state': 400, 'content': "找不到简历id, 请确认下手机号或userid填写是否正确"}
        #
        # return {
        #     'state': state,
        #     'content': info,
        #     'result': {
        #         'basicMain': basicMain,
        #         'workExperience': workExperience,
        #         'educationExperience': educationExperience,
        #         'ability_label': ability_label,
        #         'expect_jobs': r_expect_jobs
        #     }}

    def post(self):
        """修改简历信息
                @@@
                ### Author = Xiawang

                ### Request Header
                | 字段 | 值 |
                | ---- | ---- |
                | method | POST |
                | content-type | application/json |






                ### 请求示例
                ```json

                {
                    "id": 156,
                    "name": "桃花源",
                    "sex": "男",
                    "birthday": "1990.09",
                    "email": "tester2018@sina.com",
                    "liveCity": "北京",
                    "work_year": "7年",
                    "joinWorkTime": "2013.07",
                    "companyName": "拉勾网",
                    "department": "用户价值部",
                    "positionNameType1": "开发|测试|运维类",
                    "positionNameType2": "后端开发",
                    "positionType": "Python",
                    "positionName": "Python",
                    "startDate": "2018.07",
                    "endDate": "至今",
                    "companyIndustry": "新零售",
                    "skillLabel": "后端",
                    "workContent": "<p>我任职XX公司X部署在公司的私有服务器期我们基于Motan框架做了整个系统的微服务化。<br /></p>",
                    "schoolName": "北京理工大学",
                    "professional": "计算机科学与技术",
                    "ed_startDate": "2009",
                    "ed_endDate": "2012",
                    "education": "硕士",
                    "ex_positionName": "Python",
                    "ex_positionType": "全职",
                    "salarys": "10k-15k",
                    "city": "上海",
                    "status": "随便看看",
                    "arrivalTime": "2周-1个月",
                    "label_name": "演讲能力",
                    "myRemark": "<p>行我可以我最棒我最好我能行我可以我最棒我最好我能行我可以我最棒我最好<br /></p><p><br /></p>"
                }

                ```

                ### 返回
                 ```json
                    {
                        state: 1,
                        content: "基本信息修改成功！请再次查询简历信息确认是否成功"
                    }

                ```
        """
        parser = reqparse.RequestParser()
        ''' 基本信息 '''
        parser.add_argument('id', type=int, help="简历id", required=True)
        parser.add_argument('name', type=str, help="姓名")
        parser.add_argument('sex', type=str, help="性别, 例如 男、女")
        parser.add_argument('birthday', type=str, help="生日, 例如 1990.07")
        parser.add_argument('email', type=str, help="邮箱")
        parser.add_argument('liveCity', type=str, help="所在城市")
        parser.add_argument('work_year', type=str, help="工作年份")
        parser.add_argument('joinWorkTime', type=str, help="参加工作时间")
        ''' 工作经历 '''
        parser.add_argument('companyName', type=str, help="公司名称")
        parser.add_argument('department', type=str, help="所属部门")
        parser.add_argument('positionNameType1', type=str, help="一级职位类型")
        parser.add_argument('positionNameType2', type=str, help="二级类型")
        parser.add_argument('positionType', type=str, help="三级职位类型")
        parser.add_argument('positionName', type=str, help="职位名称")
        parser.add_argument('startDate', type=str, help="入职时间")
        parser.add_argument('endDate', type=str, help="离职时间")
        parser.add_argument('companyIndustry', type=str, help="行业标签")
        parser.add_argument('skillLabel', type=str, help="技能标签")
        parser.add_argument('workContent', type=str, help="工作内容")
        ''' 教育经历 '''
        parser.add_argument('schoolName', type=str, help="学校名称")
        parser.add_argument('professional', type=str, help="专业")
        parser.add_argument('ed_startDate', type=str, help="入学年份")
        parser.add_argument('ed_endDate', type=str, help="毕业年份")
        parser.add_argument('education', type=str, help="学历")
        ''' 个人名片 '''
        parser.add_argument('label_name', type=str, help="综合能力标签")
        parser.add_argument('myRemark', type=str, help="自我描述")
        ''' 求职意向 '''
        parser.add_argument('ex_positionName', type=str, help="期望职位")
        parser.add_argument('ex_positionType', type=str, help="工作性质")
        parser.add_argument('salarys', type=str, help="期望薪资")
        parser.add_argument('city', type=str, help="期望城市")
        parser.add_argument('status', type=str, choices=('积极找工作', '随便看看', '暂时不换工作'), help="当前状态")
        parser.add_argument('arrivalTime', type=str, choices=('随时', '2周以内', '2周-1个月', '1-3个月', '3个月以上'), help="到岗时间")
        args = parser.parse_args()

        info1, info2, info3, info4, info5 = '', '', '', '', ''
        effect_row = op_mysql.update_all(
            "UPDATE r_resume SET name = '%s',sex = '%s', birthday = '%s', email= '%s' , liveCity= '%s', work_year= '%s', joinWorkTime = '%s', myRemark = '%s' WHERE id = %d" % (
                args['name'], args['sex'], args['birthday'], args['email'], args['liveCity'], args['work_year'],
                args['joinWorkTime'], args['myRemark'], int(args['id'])))

        if effect_row > 0:
            info1 = '基本信息修改成功！'

        r_work_experience_effect_row = op_mysql.update_all(
            "UPDATE r_work_experience SET companyName = '%s',department = '%s',positionType1 = '%s',positionType2 = '%s',positionType='%s',positionName='%s',startDate='%s',endDate='%s',companyIndustry='%s',skillLabel='%s',workContent='%s' WHERE resumeId = %d" % (
                args['companyName'],
                args['department'],
                args['positionNameType1'],
                args['positionNameType2'],
                args['positionType'],
                args['positionName'],
                args['startDate'],
                args['endDate'],
                args['companyIndustry'],
                args['skillLabel'],
                args['workContent'],
                int(args['id'])))
        if r_work_experience_effect_row > 0:
            info2 = '工作经历修改成功! '

        r_education_experience_effect_row = op_mysql.update_all(
            "UPDATE r_education_experience SET schoolName = '%s',professional = '%s',startDate='%s',endDate='%s',education='%s' WHERE resumeId = %d" % (
                args['schoolName'], args['professional'], args['ed_startDate'], args['ed_endDate'], args['education'],
                int(args['id'])))
        if r_education_experience_effect_row > 0:
            info3 = '教育经历修改成功!'

        if args['label_name'] == '':
            r_ability_label_effect_row = op_mysql.update_all(
                "UPDATE r_ability_label SET is_del = '%s' WHERE resumeId = %d" % (1, int(args['id'])))
            if r_ability_label_effect_row > 0:
                info4 = '综合能力标签修改成功!'


        r_expect_jobs_effect_row = op_mysql.update_all(
            "UPDATE r_expect_jobs SET positionName = '%s',positionNameType1 = '%s',positionNameType2='%s',positionType='%s',salarys='%s',city='%s',status='%s',arrivalTime='%s' WHERE resumeId = %d" % (
                args['ex_positionName'], args['positionNameType1'],args['positionNameType2'], args['ex_positionType'], args['salarys'], args['city'],
                args['status'], args['arrivalTime'], args['id']))
        if r_expect_jobs_effect_row > 0:
            info5 = '求职意向修改成功'

        content = info1 + info2 + info3 + info4 + info5 + '请再次查询简历信息确认是否成功'
        if content == '':
            content = "没有修改信息哦"
        return {'state': 1, 'content': content}
