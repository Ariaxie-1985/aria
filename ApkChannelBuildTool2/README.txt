�Զ�ǩ���������2.0��

O���ر�������
��1��Python
��2��java


һ��Ŀ¼˵��:
ԭĿ¼��
/config
	|-- channel.txt  			������ʶ��һ����ʶռһ�С�
	|-- LagouAndroid.keystore 	        ����ǩ���������޸�
	|-- tmp.txt 				��ʱ�ļ�����ɾ�������޸�
/srcApks					δǩ����Դ�ļ�Ŀ¼�����ӹ̺��apk�ļ�Ŀ¼
/targetApks				        ����ǩ����������������apkĿ¼
ApkBuilder.py  					ǩ�����������ű���˫��ִ��
zipalign.exe					���빤��
����Ϊ����Ŀ¼��
/common jiaguapk                                 ������������ϴ�common���������������������������ӹ̺��common���ڴ��ļ�����
xxxx.xlsx                                        �����ļ����������յ�����������Ե���������������0912.xlsx
clear.py                                         ����������ϵ��ϰ汾��������Ϊ��ǰ�汾���ݵ������汾
dsu.py                                           dsu�����㷨������汾�ŵ���������
getChannel.py                                    ��ȡ�����ļ�
common.py                                        ��װ�����õ��ķ���
startBuild.py                                    ִ�����յ��������ֱ��ִ�д��ļ�
aapt.exe                                         ��׿aapt���ߣ����ڻ�ȡapk��Ϣ                                    
OtherChannel.xlsx                                ���ó�common��֮��Ĵ������
other jiaguapk                                   ��common����������������������֮��İ����ӹ̺���ڴ��ļ���

OtherChannel.xlsxʹ��˵����
1.�����ؼ��ְ��������֣��ؼ����Լ��ӹ̷�ʽ���ö��Ÿ���
2.������Ϊ�ð���Ҫ�������������������ö��ŷָ�
3.����other jiaguapk�ļ����е�apk����Ӧ��ñ�������ͬ����������ͷ��                                                  
                                           
�����Ҷ�������������裨ֻ��1���򼸸�������ͬ�˲��裩
1������apk
	������ǩ����apk��
2���ӹ�
	��1���ɵ�apk��common��������360�ӹ̣�һ��ʹ��Ĭ�ϼӹ����ã�ԭ����Ҳ����ʹ�ðٶȼӹ̣�
	360�ӹ̣�http://jiagu.360.cn/            hhf2009b@163.com   ranfeng0610
	�ٶȼӹ̣�http://app.baidu.com/jiagu/    vivi@lagou.com   vivi@0911
3��ǩ����������
��1��config/channel.txt���޸Ķ�Ӧ������Ϊ��lagou-hdcs
��2����2�ӹ̺��apk����srcApksĿ¼��
��3��ִ��ApkBuilder.py 
��4��/targetApksĿ¼�µ�apk�����������������

�������շ����������������
1������apk
	������ǩ����apk��
2���ӹ�
        ��1���ɵ�apk��common�����ֱ����360�ӹ̺Ͱٶȼӹ̣�һ��ʹ��Ĭ�ϼӹ�����
	��1���ɵ�apk����common�����ֱ���OtherChannel.xlsx��¼���мӹ�
        360�ӹ̣�http://jiagu.360.cn/            hhf2009b@163.com   ranfeng0610
	�ٶȼӹ̣�http://app.baidu.com/jiagu/    vivi@lagou.com   vivi@0911
3��ǩ����������
��1����2���ɵ�����apk�����������ɲο���������������360�ӹ̵İ��������������360�����ٶȼӹ̵İ��������������baidu������common����ͬʱ����OtherChannel.xlsx�еĹؼ���
��2���������������common apk����common jiaguapkĿ¼�У���common apk����other jiaguapk��
��3����������ļ������Ƿ��ǵ�������
��4����鵱ǰ���������Ƿ���㣬�����20G������Ͽ�vpn���رյ���wifi��ʹ���������ӣ������ϴ��ٶȼ�����
��5��ִ��startBuild.py���ڼ���Կ��ܻ�ܿ�
��6��ִ����Ϻ����\\file.oss.lagou.com\config\ACP\android-c ȷ���Ƿ�ɹ�������config71c9c��
