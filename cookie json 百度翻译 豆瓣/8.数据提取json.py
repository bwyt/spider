"""
json --> dict

dict --> json

json --> 文件

读取json文件

"""
import json

json_str = '{"user":"zs","age":18}'
print('json_str：',json_str)
dic = json.loads(json_str)
print('dic：',dic)

jso = json.dumps(dic, ensure_ascii=False, indent=2)
print(jso)

#
# with open('demo.json', 'w', encoding='utf-8') as f:
#     json.dump(jso, f, ensure_ascii=False)
#
with open('demo.json', 'r', encoding='utf-8') as f:
    json.load(f, ensure_ascii=False)