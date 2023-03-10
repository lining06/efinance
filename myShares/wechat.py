import json

import requests
msg = 'Hello World'
data = {
            "msgtype": "text",
            "text": {
                "content": msg,
                "mentioned_mobile_list": ["13681953758"]
            }
        }
r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=80367921-d43c-4b87-bb6a-1628b9bb7e6f',
                  data=json.dumps(data))
r