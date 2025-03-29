# 清除列队/无返回信息则为成功
# POST http://192.168.3.25:8188/queue
import http.client
import json

conn = http.client.HTTPConnection("localhost", 8188)
payload = json.dumps({
   "clear": True
})
headers = {
   'Content-Type': 'application/json'
}
conn.request("POST", "/queue", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
