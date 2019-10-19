from django.shortcuts import render, redirect, render_to_response
import requests
from bs4 import BeautifulSoup
import re
# Create your views here.


def index(requst):
    jsonReturn = {'WarehouseAddress': main()}
    return render_to_response('../templates/index.html', jsonReturn)
    return render(requst,"../templates/index.html")


def main():
    jsonArr=[]
    # jsonList={"仓库地址："："","仓库名称":"","获取说明文字:":"","语言 类型:":""}
    indexs=-1
    url = 'https://github.com/trending'
    html = requests.get(url)
    html.encoding = 'utf-8'
    html_gy = html.text
    bf = BeautifulSoup(html_gy, 'html.parser',from_encoding='utf-8')
    box_row_url = bf.find_all(class_="Box-row")
    #print(box_row_url)
    # hero_name=list(map(lambda x:x['cname'],html.json()))
    # hero_number=list(map(lambda x:x['ename'],html.json()))
    for mneach in box_row_url:
        jsonList={}
        indexs += 1
        box_row_h1=mneach.find_all('h1',class_='h3 lh-condensed')
        box_row_p = mneach.find_all("p")
        box_row_div = mneach.find_all('div')
        # print(box_row_div)
        # 获取项目仓库地址
        for reap_Links in box_row_h1:
            # aherf=links.find_all("a")
            reop_ahref = str('https://www.github.com') + reap_Links.a.get('href')
            # jsonList["仓库地址："]=str(reop_ahref)
            # jsonList["仓库名称"]=str(reop_ahref)
            WarehouseNameIndex=str(reop_ahref).rindex('/')
            WarehouseName=str(reop_ahref)[WarehouseNameIndex+1:]

            jsonList['仓库地址:'] = str(reop_ahref)
            jsonList['仓库名称:']=WarehouseName
            # jsonArr.append(jsonList)
            # print("仓库地址：", str(reop_ahref), "\n仓库名称：",str(reap_Links.a.text).split('/')[1])

            print(indexs,"你好")
        # 获取说明文字
        for reop_Content in box_row_p:
            content=reop_Content.text
            jsonList['获取说明文字:']=str(content)
            print("获取说明文字:", str(content))

        # 获取下面的语言 star数等内容
        for reop_Bottom in box_row_div:
            # reop_ahref = str('https:www.github.com/') + reopLinks.a.get('href')
            bottomL = reop_Bottom.find_all('span',class_ = 'd-inline-block ml-0 mr-3')
            for btoL in bottomL:
                # 获取语言 类型
                Language = btoL.find(itemprop = 'programmingLanguage').text
                jsonList['语言 类型:']=str(Language)
                print("语言 类型:", str(Language))

            bottomZ = reop_Bottom.find_all('a', class_='muted-link d-inline-block mr-3')
            # bottomZsvg1 = reop_Bottom.find_all('svg', class_='octicon octicon-star')
            # bottomZsvg2 = reop_Bottom.find_all('svg', class_='octicon octicon-repo-forked')
            # print(bottomZ)
            # 循环的是bottomZ中的子元素的个数

            dr = re.compile(r'<[^>]+>', re.S)
            dd = dr.sub('', str(bottomZ))
            jsonList['star数：']=dd
            jsonList['Fork数：']=dd

            # for btoZ in bottomZ:
            #     # 获取 点赞数
            #     bto = btoZ.text
            #     jsonList['Fork数：']=bto
            #     s=get_number(bto)
            #     print(s)
            # # print(bottoms)
        jsonArr.append(jsonList)

    return jsonArr

# def get_number(x):
#     return float(filter(str.isdigit, str(x)))

ss = main()
for a in ss:
    print(a)