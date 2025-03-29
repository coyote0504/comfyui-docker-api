# 获取系统中所有组件以及可用参数
# GET http://192.168.3.25:8188/object_info

import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("GET", "/object_info", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
