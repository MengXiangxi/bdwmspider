# -*- coding: UTF-8 -*-
from urllib import request
import time


def html_parse(html_content):
    html_len = len(html_content)
    uname = ""
    for i in range(0, html_len):
        line_content = html_content[i].strip().decode('utf-8')
        if line_content.find("bbsid") >= 1:
            uname = line_content[20:-7]
        if line_content == "<label>性别：</label>":
            gender = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>星座：</label>":
            zodiac = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>上站次数：</label>":
            login_num = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>发帖数：</label>":
            post_nun = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>生命力：</label>":
            life = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>积分：</label>":
            integral = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>原创分：</label>":
            original = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>最近上站时间：</label>":
            last_seen = html_content[i+1].strip().decode('utf-8')[:-14]
    if len(uname) < 1:
        return ""
    else:
        return uname+","+gender+","+zodiac+","+login_num+","+post_nun+","+life+","+integral+","+original+","+last_seen+"\n"


buffer = ""
time_stamp = time.time()

for i in range(1, 110000):
    target_url = "http://bbs.pku.edu.cn/v2/user.php?uname="+str(i)
    try:
        response = request.urlopen(target_url)
    except:
        print("Error in No."+str(i))
        with open("err.txt", "a") as errfile:
            errfile.write(target_url+"\n")
            next
    html_content = response.readlines()
    parse_line = html_parse(html_content)
    buffer += parse_line
    if i % 100 == 0:
        print(i)
        print(str(time.time()-time_stamp))
        time_stamp = time.time()
        with open("user_profile.csv", "a", encoding="utf-8") as userfile:
            userfile.write(buffer)
        buffer = ""
