# -*- coding: UTF-8 -*-
from urllib import request
import time

def html_parse(uid, html_content):
    html_len = len(html_content)
    uname = ""
    duty = "user"
    vip = "NA"
    for i in range(0, html_len):
        line_content = html_content[i].strip().decode('utf-8')
        if line_content.find("bbsid") >= 1:
            uname = line_content[20:-7]
        if line_content.find("class=\"personal-duty\"") >=1:
            duty = line_content[33:-7]
        if line_content.find("class=\"vip\"") >= 1:
            vip = line_content[48]
        if line_content == "<label>性别：</label>":
            gender = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>星座：</label>":
            zodiac = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>上站次数：</label>":
            login_num = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>发帖数：</label>":
            post_num = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>生命力：</label>":
            life = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>积分：</label>":
            user_score = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>原创分：</label>":
            original = html_content[i+1].strip().decode('utf-8')[:-14]
        if line_content == "<label>最近上站时间：</label>":
            last_seen = html_content[i+1].strip().decode('utf-8')[:-14]
    if len(uname) < 1:
        return ""
    else:
        out_list = [str(uid), uname, gender, zodiac, login_num, post_num, 
                    life, user_score, original, last_seen, duty, vip]
        return ",".join(out_list)+"\n"

class RedirectFilter(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, hdrs, newurl):
        if newurl.endswith('.jpg'):
            return None # do not redirect, HTTPError will be raised
        return request.HTTPRedirectHandler.redirect_request(self, req, fp, code, msg, hdrs, newurl)

buffer = ""
time_stamp = time.time()
opener = request.build_opener(RedirectFilter)

for i in range(40000, 40010):
    target_url = "http://bbs.pku.edu.cn/v2/user.php?uid="+str(i)
    try:
        response = request.urlopen(target_url)
        #response = opener.open(target_url)
    except:
        print("Error in No."+str(i))
        with open("err.txt", "a") as errfile:
            errfile.write(target_url+"\n")
        continue
    html_content = response.readlines()
    parse_line = html_parse(i, html_content)
    buffer += parse_line
    if i % 1 == 0:
        print(parse_line[:-1])
        print(str(time.time()-time_stamp))
        time_stamp = time.time()
        with open("user_profile.csv", "a", encoding="utf-8") as userfile:
            userfile.write(buffer)
        buffer = ""
