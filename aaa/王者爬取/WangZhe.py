import json

import requests
# 一.确定爬取的url路径，分析目标网页
base_url = 'https://pvp.qq.com/web201605/js/herolist.json'

# 二.发送请求，通过requests模块，获取响应数据
response = requests.get(base_url)
data_str = response.text
# print(data_str)

# 三.解析数据

    # "ename": 105, 这个就是英雄的id
	# "cname": "廉颇",  这个是英雄的名字 保存文件数据的时候需要英雄的名字
	# "title": "正义爆轰",
	# "new_type": 0,
	# "hero_type": 3,
	# "skin_name": "正义爆轰|地狱岩魂" 这个是英雄的皮肤名称，当前这个英雄只有两个名称，所# 以有两个皮肤，保存文件时需要切割

    # 1.将json字符串转换成列的数据
data_list = json.loads(data_str)
# print(type(data_list))
for data in data_list:
    # print(data)

    ename = data['ename'] # 英雄的编号
    cname =data['cname'] # 英雄的名称
    try:

        skin_name = data['skin_name'].split('|') # 英雄皮肤的名称
    except Exception as e:
        print(e)
    print(ename, cname, skin_name)


# 构建图片的url地址
    #
    for skin_num in range(1, len(skin_name) + 1):
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
            ename) + '-bigskin-' + str(skin_num) + '.jpg'
        print(skin_url)

    # 再次调用requests的库进行图片的获取，因为当前这个图片是一个二进制数据。所以要调用content方法进行提取
        shin_data = requests.get(skin_url).content
    # 保存数据 --保存再目标文件中
    # 由于图片是二进制的所以要选择的方式是wb
        with open('img\\'+cname+'-'+skin_name[skin_num-1]+'.jpg',mode='wb') as f:
            # print("打印正在下载的图片"+ename+'-'+skin_name[skin_num-1])
            f.write(shin_data)