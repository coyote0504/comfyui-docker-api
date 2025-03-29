# 图片的在线预览接口（上传图像，生图图像，蒙蔽图像，均通过该接口预览）
# GET http://192.168.3.25:8188/view
import http.client

conn = http.client.HTTPConnection("localhost", 8188)
output_name = "ComfyUI_00001_.png"  # Replace with your actual output name
payload = ''
headers = {}
# filename string 图片名称 示例值: SVD_img2vid_00030.gif 必需
# type string  图片存放位置的文件夹（input为长传图片，output为生成的图片） 示例值: output 可选
# subfolder string 子文件夹(没有可不填) 可选
# preview string 预览 示例值: WEBP 可选
# channel string 示例值: rgb 可选
conn.request("GET", f"/view?{output_name}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
