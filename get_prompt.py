# 获取服务器当前剩余任务列队的数量
# GET http://192.168.3.25:8188/prompt
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("GET", "/prompt", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
