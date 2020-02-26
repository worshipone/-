#coding:utf-8
import pymongo
from pymongo import MongoClient
import snownlp
from snownlp import SnowNLP
from snownlp import sentiment
names = ['1月1日-1月2日','1月3日-1月4日','1月5日-1月6日','1月7日-1月8日','1月9日-1月10日','1月11日-1月12日','1月13日-1月14日','1月15日-1月16日','1月17日-1月18日','1月19日-1月20日','1月21日-1月22日','1月23日-1月24日','1月25日-1月26日','1月27日-1月28日','1月29日-1月30日','1月31日-2月1日','2月2日-2月3日','2月4日-2月5日','2月6日-2月7日','2月8日-2月9日','2月10日-2月11日','2月12日-2月13日','2月14日-2月15日','2月16日-2月17日','2月18日-2月19日']
pros=['河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南','四川','贵州','云南','陕西','甘肃','青海','北京','天津','上海','重庆','广西','内蒙古','西藏','宁夏','新疆','澳门','海外','台湾','香港']
client = MongoClient('localhost', 27017)  # 链接数据库
for pro in pros:
    a = 0
    total=0
    for name in names:
        db = client[name]  # 匹配Taoguba表
        news = db.Comments
        for i in news.find({"province": pro}):
            f = open("{}评论.txt".format(pro), mode='a', encoding="utf-8")
            string=i['content']
            if string == '':
                pass
            else:

                f.write(string)
                s=SnowNLP(string)
                total=total+s.sentiments
                a = a + 1
    print("{}有{}人评论".format(pro,a))
    print(total/a)
