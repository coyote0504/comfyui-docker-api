# 系统统计信息接口
# GET http://192.168.3.25:8188/system_stats
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("GET", "/system_stats", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
