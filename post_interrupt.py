# 取消当前任务/不需任何参数
# POST http://192.168.3.25:8188/interrupt
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("POST", "/interrupt", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
