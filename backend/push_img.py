# -*- coding: utf-8 -*-
import oss2
import os
from oss2.credentials import EnvironmentVariableCredentialsProvider

# 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。
# 设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET
# OSS_ACCESS_KEY_ID = "LTAI5tR1c1uhFRfWxjq8BWT4"
# OSS_ACCESS_KEY_SECRET = "BdN5OIEdet7IO6KWOq7TJiivHOsC5B"
auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider())
# yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
# 填写Bucket名称。
bucket = oss2.Bucket(auth, 'https://oss-cn-beijing.aliyuncs.com', 'graphcrafter')

# 必须以二进制的方式打开文件。
# 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。
with open('C:\\Users\\h1585\\Pictures\\核心硬件评测.png', 'rb') as fileobj:
    fileobj.seek(0, os.SEEK_SET)
    # Tell方法用于返回当前位置。
    current = fileobj.tell()
    # 填写Object完整路径。Object完整路径中不能包含Bucket名称。
    bucket.put_object('核心硬件评测.png', fileobj)
