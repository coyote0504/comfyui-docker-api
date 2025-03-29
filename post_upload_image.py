# 上传图片接口
# POST http://192.168.3.25:8188/upload/image
import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("localhost", 8188)
dataList = []
image_name = 'ComfyUI_00015_.png'
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=image; filename={0}'.format(image_name)))

fileType = mimetypes.guess_type(image_name)[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open(image_name, 'rb') as f:
   dataList.append(f.read())
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/upload/image", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
