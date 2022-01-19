# CBC-Policy-Operations

Prod06 Examples Only

To import all policy, run import_all.py

Usage:

Import:
python policy_operations.py --cburl https://api-prod06.conferdeploy.net --apitoken AAAAAAAAAAAAAAAAAAAAAAAA/BBBBBBBBBB import -N "01 Good Protection" -d "" -p "MEDIUM" -f 01_Good_Protection.json

Export:
python policy_operations.py --cburl https://api-prod06.conferdeploy.net --apitoken AAAAAAAAAAAAAAAAAAAAAAAA/BBBBBBBBBB export -N "Windows Standard | TST"
