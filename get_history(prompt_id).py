# 获取历史任务数据(根据任务prompt_id获取历史数据)
# GET http://192.168.3.25:8188/history/0593b3cc-a51c-4791-af75-16dfc623101a
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
payload = ''
prompt_id = "0593b3cc-a51c-4791-af75-16dfc623101a"  # Replace with your actual prompt ID
headers = {}
conn.request("GET", f"/history/{prompt_id}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
