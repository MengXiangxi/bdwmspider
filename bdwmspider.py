# -*- coding: UTF-8 -*-
'''
bdwmspider

20180126 v1.0
Obtaining user profile from bdwm.net
https://github.com/MengXiangxi/bdwmspider
'''
import pycurl
from io import BytesIO
import time
# import certifi # for certification problems 1/2

def html_parse(uid, html_content):
    '''Pasing the html contents'''
    html_len = len(html_content)
    uname = ""
    duty = "user"
    vip = "NA"
    for i in range(0, html_len):
        line_content = html_content[i].strip()
        if line_content.find("bbsid") >= 1:
            uname = line_content[20:-7]
        if line_content.find("class=\"personal-duty\"") >=1:
            duty = line_content[33:-7]
        if line_content.find("class=\"vip\"") >= 1:
            vip = line_content[48]
        if line_content == "<label>性别：</label>":
            gender = html_content[i+1].strip()[:-14]
        if line_content == "<label>星座：</label>":
            zodiac = html_content[i+1].strip()[:-14]
        if line_content == "<label>上站次数：</label>":
            login_num = html_content[i+1].strip()[:-14]
        if line_content == "<label>发帖数：</label>":
            post_num = html_content[i+1].strip()[:-14]
        if line_content == "<label>生命力：</label>":
            life = html_content[i+1].strip()[:-14]
        if line_content == "<label>积分：</label>":
            user_score = html_content[i+1].strip()[:-14]
        if line_content == "<label>原创分：</label>":
            original = html_content[i+1].strip()[:-14]
        if line_content == "<label>最近上站时间：</label>":
            last_seen = html_content[i+1].strip()[:-14]
    if len(uname) < 1:
        return ""
    else:
        out_list = [str(uid), uname, gender, zodiac, login_num, post_num, 
                    life, user_score, original, last_seen, duty, vip]
        return ",".join(out_list)+"\n"

buffer = ""
time_stamp = time.time() # calculate time elapsed

for i in range(2601, 35000): # range to grab
    target_url = "https://bbs.pku.edu.cn/v2/user.php?uid="+str(i)
    try:
        curl_buffer = BytesIO()
        c = pycurl.Curl()
        # c.setopt(pycurl.CAINFO, certifi.where()) # for certification problems 2/2
        c.setopt(c.URL, target_url)
        c.setopt(c.WRITEDATA, curl_buffer)
        c.perform()
        c.close()
        body = curl_buffer.getvalue()
    except:
        print("Error in No."+str(i))
        with open("err.txt", "a") as errfile:
            errfile.write(target_url+"\n")
        continue
    html_content = body.decode("utf-8").split('\n')
    parse_line = html_parse(i, html_content)
    buffer += parse_line
    if i % 100 == 0:
        print(i)
        print(str(time.time()-time_stamp))
        time_stamp = time.time()
        with open("user_profile.csv", "a", encoding="utf-8") as userfile:
            userfile.write(buffer)
        buffer = ""