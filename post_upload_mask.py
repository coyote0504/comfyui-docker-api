# 上传蒙版图片接口，一般用于局部重绘
# POST http://192.168.3.25:8188/upload/mask

# image file 图片将以二进制格式发送到服务器 示例值: file://C:\Users\dourungeng\Pictures\640.png 必需
# type string 上传图片的目标文件夹 示例值: input 可选
# subfolder string 上传图片的目标子文件夹 示例值: clipspace 可选
# original_ref string 原图的引用信息 示例值: {“filename”:”640.png”,”type”:”input”,”subfolder”:”clipspace”} 可选
import http.client
import mimetypes
import os
import json
from codecs import encode

conn = http.client.HTTPConnection("localhost", 8188)
dataList = []

# 修复路径格式问题
mask_path = r'C:\Users\dourungeng\Pictures'  # 使用原始字符串
mask_name = '640.png'
mask_full_path = os.path.join(mask_path, mask_name)  # 正确拼接路径

boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=image; filename={0}'.format(mask_name)))  # 只传文件名而不是完整路径

fileType = mimetypes.guess_type(mask_full_path)[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open(mask_full_path, 'rb') as f:  # 使用正确拼接的路径
   dataList.append(f.read())
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=original_ref;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

# 正确构造JSON，使用变量
original_ref = json.dumps({"filename": mask_name, "type": "input", "subfolder": "clipspace"})
dataList.append(encode(original_ref))

dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/upload/mask", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
