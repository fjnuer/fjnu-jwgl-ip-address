#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

def website_status(url):
    req = urllib.request.Request(url)
    try:
        res = urllib.request.urlopen(req, timeout=10)
        if 200 == res.getcode():
            return True
    except urllib.error.URLError as e:
        # print(e.reason)
        return False
        
if __name__ == '__main__': 
    ip_address = [
        '59.77.193.21',
        '10.128.14.1',
        '10.128.14.6',
        '10.128.14.7',
        '10.128.14.8',
        '10.128.14.9',
        '10.128.14.10',
        '10.128.14.11',
        '10.128.14.12',
        '10.128.14.13',
        '10.128.14.14',
        '10.128.14.15',
        '10.128.14.17',
        '10.128.14.18',
        '10.128.14.19',
        '10.128.14.20'

    # 尝试获取验证码框，HTTP Status Code 为 200 时访问正常。
    for ip in ip_address:
        url = 'http://' + ip + '/CheckCode.aspx'
        if website_status(url):
            print('[OK] IP ' , ip, '访问正常。')
        else:
            print('[WARNING] IP ' , ip, '访问异常。')




