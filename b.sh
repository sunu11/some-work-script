#!/bin/bash
#by s
#使用方法：
# chmod +x b.sh 
#./b.sh input information
#如果报错，先使用yum install ufw 下载ufw




echo -n  "please enter White_ip and Hi_risk_port ->"
read  v1 v2

echo "White_ip = $v1"
echo "Hi_risk_port = $v2"
ufw enable
ufw allow from $v1 to any port $v2
ufw status
