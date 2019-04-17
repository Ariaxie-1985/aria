自动签名打包工具2.0版

O、必备环境：
（1）Python
（2）java


一、目录说明:
原目录：
/config
	|-- channel.txt  			渠道标识，一个标识占一行。
	|-- LagouAndroid.keystore 	        拉勾签名。无需修改
	|-- tmp.txt 				临时文件。勿删。无需修改
/srcApks					未签名的源文件目录。即加固后的apk文件目录
/targetApks				        生成签完名并打完渠道的apk目录
ApkBuilder.py  					签名并打渠道脚本，双击执行
zipalign.exe					对齐工具
以下为新增目录：
/common jiaguapk                                 用于批量打包上传common包（主包，名称是拉勾），将加固后的common包在此文件夹下
xxxx.xlsx                                        渠道文件，用于最终的批量打包，以当天日期命名，如0912.xlsx
clear.py                                         清理服务器上的老版本渠道包，为当前版本上溯第六个版本
dsu.py                                           dsu排序算法，解决版本号的排序问题
getChannel.py                                    读取渠道文件
common.py                                        封装可能用到的方法
startBuild.py                                    执行最终的批量打包直接执行此文件
aapt.exe                                         安卓aapt工具，用于获取apk信息                                    
OtherChannel.xlsx                                配置除common包之外的打包规则
other jiaguapk                                   除common包（主包，名称是拉勾）之外的包，加固后放在此文件夹

OtherChannel.xlsx使用说明：
1.包名关键字包含两部分，关键字以及加固方式，用逗号隔开
2.渠道号为该包需要打的渠道，多个渠道号用逗号分隔
3.最终other jiaguapk文件夹中的apk个数应与该表行数相同（不包括表头）                                                  
                                           
二、灰度用渠道打包步骤（只打1个或几个渠道包同此步骤）
1、生成apk
	生成已签名的apk。
2、加固
	将1生成的apk（common包）进行360加固，一般使用默认加固配置（原则上也可以使用百度加固）
	360加固：http://jiagu.360.cn/            hhf2009b@163.com   ranfeng0610
	百度加固：http://app.baidu.com/jiagu/    vivi@lagou.com   vivi@0911
3、签名并打渠道
（1）config/channel.txt中修改对应渠道号为：lagou-hdcs
（2）将2加固后的apk放入srcApks目录中
（3）执行ApkBuilder.py 
（4）/targetApks目录下的apk即本次所打的渠道包

三、最终发布用渠道打包步骤
1、生成apk
	生成已签名的apk。
2、加固
        将1生成的apk（common包）分别进行360加固和百度加固，一般使用默认加固配置
	将1生成的apk（非common包）分别按照OtherChannel.xlsx记录进行加固
        360加固：http://jiagu.360.cn/            hhf2009b@163.com   ranfeng0610
	百度加固：http://app.baidu.com/jiagu/    vivi@lagou.com   vivi@0911
3、签名并打渠道
（1）将2生成的两个apk进行命名，可参考以往命名，其中360加固的包命名必须包含“360”，百度加固的包命名必须包含“baidu”，非common包需同时包含OtherChannel.xlsx中的关键字
（2）将命名后的两个common apk放入common jiaguapk目录中，非common apk放入other jiaguapk中
（3）检查渠道文件命名是否是当天日期
（4）检查当前磁盘容量是否充足，需大于20G，建议断开vpn，关闭电脑wifi，使用网线连接（否则上传速度极慢）
（5）执行startBuild.py，期间电脑可能会很卡
（6）执行完毕后进入\\file.oss.lagou.com\config\ACP\android-c 确认是否成功（密码config71c9c）
