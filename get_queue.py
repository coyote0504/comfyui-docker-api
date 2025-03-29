# 获取任务队列数量
# GET http://192.168.3.25:8188/queue
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("GET", "/queue", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
