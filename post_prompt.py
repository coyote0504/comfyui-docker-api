# 绘图任务的下发接口，此接口只做任务下发，返回任务ID信息。
# POST http://192.168.3.25:8188/prompt
import http.client
import json

conn = http.client.HTTPConnection("localhost", 8188)

# 添加外层结构
prompt_data = {
    "prompt": {
        "1": {
            "inputs": {
                "text": "text, watermark",
                "clip": [
                    "7",
                    1
                ]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
                "title": "CLIP文本编码"
            }
        },
        "2": {
            "inputs": {
                "text": "Childlike hand-drawn illustration in picture book style. Four adorable kindergarten children with slightly oversized heads and big expressive eyes sitting under bamboo trees having a picnic. Simple, spacious park background with green grass and few bamboo stalks. Cheerful spring sunlight. A little girl excitedly holding up a wooden box with simple lychee pattern that emits a faint glow. Other children looking curious with exaggerated expressions. Fresh bright colors: soft green, light blue, gentle yellow. Deliberately imperfect childlike lines and shapes. Composition leaves space at top and bottom for text, <lora:ChildrensBookStyle:0.8>, <lora:WatercolorSoft:0.6>, <lora:HandDrawnIllustration:0.7>, <lora:SimpleJoy:0.5>",
                "clip": [
                    "7",
                    1
                ]
            },
            "class_type": "CLIPTextEncode",
            "_meta": {
                "title": "CLIP文本编码"
            }
        },
        "3": {
            "inputs": {
                "width": 512,
                "height": 512,
                "batch_size": 1
            },
            "class_type": "EmptyLatentImage",
            "_meta": {
                "title": "空Latent图像"
            }
        },
        "4": {
            "inputs": {
                "seed": 981019041665457,
                "steps": 20,
                "cfg": 8,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1,
                "model": [
                    "7",
                    0
                ],
                "positive": [
                    "2",
                    0
                ],
                "negative": [
                    "1",
                    0
                ],
                "latent_image": [
                    "3",
                    0
                ]
            },
            "class_type": "KSampler",
            "_meta": {
                "title": "K采样器"
            }
        },
        "5": {
            "inputs": {
                "samples": [
                    "4",
                    0
                ],
                "vae": [
                    "7",
                    2
                ]
            },
            "class_type": "VAEDecode",
            "_meta": {
                "title": "VAE解码"
            }
        },
        "6": {
            "inputs": {
                "filename_prefix": "ComfyUI",
                "images": [
                    "5",
                    0
                ]
            },
            "class_type": "SaveImage",
            "_meta": {
                "title": "保存图像"
            }
        },
        "7": {
            "inputs": {
                "ckpt_name": "sd_xl_base_1.0.safetensors"
            },
            "class_type": "CheckpointLoaderSimple",
            "_meta": {
                "title": "Checkpoint加载器（简易）"
            }
        }
    },
    "client_id": "python_client"  # 添加客户端ID
}

payload = json.dumps(prompt_data)
headers = {
   'Content-Type': 'application/json'
}
conn.request("POST", "/prompt", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
