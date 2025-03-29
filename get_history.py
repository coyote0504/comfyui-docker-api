# 获取历史任务列表
# GET http://192.168.3.25:8188/history
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("GET", "/history", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
