# 根据组件名称获取系统中组件参数
# GET http://192.168.3.25:8188/object_info/KSampler
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
headers = {}
conn.request("GET", "/object_info/KSampler", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
