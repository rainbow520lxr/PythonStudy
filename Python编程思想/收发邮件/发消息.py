#!/usr/local/bin/python
#-*- coding:utf-8 -*-
import http.client
import urllib

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#用户名是登录用户中心->验证码短信->产品总览->APIID
account  = "C80900153"
#密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "8dbfb74d24a8586130a94717e5a36d85"

def send_sms(text, mobile):
    params = urllib.parse.urlencode({'account': account, 'password' : password, 'content': text, 'mobile':mobile,'format':'json' })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':

    mobile = "18982212076"
    #暂时不能改格式
    text = "您的验证码是：520。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))