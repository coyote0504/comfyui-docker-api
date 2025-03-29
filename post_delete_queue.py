# 删除列队/无返回信息则为成功
# POST http://192.168.3.25:8188/queue
import http.client
import json

conn = http.client.HTTPConnection("localhost", 8188)
prompt_id = "0593b3cc-a51c-4791-af75-16dfc623101a"  # Replace with your actual prompt ID
payload = json.dumps({
   "delete": prompt_id
})
headers = {
   'Content-Type': 'application/json'
}
conn.request("POST", "/queue", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
