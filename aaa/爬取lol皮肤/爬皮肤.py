# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@TIME: 2021/3/12 9:16
# !@Author : 提不动刀的胖虎
# !@File :.py
import json
import os
import requests
# 一.确定爬取的url路径，分析目标网页
#安妮的第一个皮肤https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg
#安妮的第二个皮肤https://game.gtimg.cn/images/lol/act/img/skin/big1001.jpg
#安妮的第三个皮肤https://game.gtimg.cn/images/lol/act/img/skin/big1002.jpg

#狂战士第一个皮肤https://game.gtimg.cn/images/lol/act/img/skin/big2000.jpg
#狂战士第二个皮肤https://game.gtimg.cn/images/lol/act/img/skin/big2001.jpg

#{
#            "heroId":"1",
#            "name":"黑暗之女",
#            "alias":"Annie",
#           "title":"安妮",
#          "roles":[
#             "mage"
#        ],
#       "isWeekFree":"0",
#      "attack":"2",
#            "defense":"3",
#            "magic":"10",
#            "difficulty":"6",
#            "selectAudio":"https://game.gtimg.cn/images/lol/act/img/vo/choose/1.ogg",
#            "banAudio":"https://game.gtimg.cn/images/lol/act/img/vo/ban/1.ogg",
#            "isARAMweekfree":"0",
#            "ispermanentweekfree":"0",
#            "changeLabel":"无改动",
#            "goldPrice":"4800",
#            "couponPrice":"2000",
#            "camp":"",
#            "campId":"",
#            "keywords":"安妮,黑暗之女,火女,Annie,anni,heianzhinv,huonv,an,hazn,hn"
#        }

#base_url = 'https://pvp.qq.com/web201605/js/herolist.json'
base_url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
# 二.发送请求，通过requests模块，获取响应数据
herolist = requests.get(base_url)
herolist_json = herolist.json()

heroId = list(map(lambda x:x['heroId'],herolist_json['hero']))#提取英雄Id

for heroid in heroId:

	herojs_url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js".format(heroid)
	herojs = requests.get(herojs_url).json()
	heroname = herojs['hero']['name'] + herojs['hero']['title']
	try:
		os.mkdir(heroname)#创建英雄文件夹
		print("\n\n[+] 文件夹【{}】创建成功，开始下载皮肤".format(heroname))
	except FileExistsError:
		print("\n\n[!] 文件夹【{}】已存在，开始下载皮肤".format(heroname))

	for skin in herojs['skins']:
		skinname = skin['name']#提取皮肤名称
		print("[-] 正在下载【{}】".format(skinname))
		skinurl = skin['mainImg']#提取皮肤链接
		#炫彩皮肤错误处理
		try:
			skin_jpg = requests.get(skinurl)
			if skin_jpg.status_code == 200:
				f = open(heroname+"\\"+skinname+".jpg","wb")
				f.write(skin_jpg.content)
				f.close()
		except:
			print(format(skinname))
