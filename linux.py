import json
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
headers = {'Content-Type': 'application/json'}
headers = {'X-WSSE': 'UsernameToken Username="N/A",PasswordDigest="rTMQAgicPUkUnmfpS5U0b6ctfGzHUrTbVpYZxshmlg8=",SdkName=wgSdk,Nonce="C22EDD3B6A33AF309E4C4667A53B4364",Timestamp="2021-07-03T02:11Z"'}
datas = json.dumps({"data":"aWSL%2FCUzuyPbCy%2FW13xWEV8NlfFpMSbx1T30vRHELNgTSZRFOGTqJ8LclFQGyRI2CK0ByM%2BOaZjIoLAoKkg19g%3D%3D"})
r = requests.post("https://oms.flow.wostore.cn/server/achieve/shouting/config/api/v1", data=datas, headers=headers)
print(r.text)
with open ('1.txt','w') as file:
 file.write(r.text)