# coding:utf-8
# @Time  : 2018-12-29 13:02
# @Author: Xiawang

import yaml
import os


def get_yaml_test_data(yamlfile):
	# 获取当前脚本所在文件夹路径
	if os.name == "nt":
		# windows系统获取
		curPath = os.getcwd() + "\\tests\\testdata"
	else:
		curPath = os.getcwd() + "/tests/testdata"

	# 获取yaml文件路径
	yamlPath = os.path.join(curPath, yamlfile)
	# open方法打开直接读出来
	cfg = open(yamlPath, 'r', encoding='utf-8').read()
	return yaml.load(cfg)  # 用load方法转字典

