"""
数据提取
	从响应中提取需要的数据的过程
    
数据分类
		非结构化数据：html,使用正则或者xpath提取
		结构化数据：json,使用json,或者jsonpath提取

json
	概念：是一种轻量级的数据格式
	应用：前后台的数据交换
	参数：ensure_ascii是否使用ascii码表,indent=2缩进层级
"""
import json

# json --> dict --> json.loads(json格式数据)
json_str = '{"user":"zs","age":18}'
print('json_str：',json_str)
dic = json.loads(json_str)
print('dic：',dic)

# dict --> json --> json.dumps(python代码格式)
jso = json.dumps(dic, ensure_ascii=False, indent=2)
print(jso)

# json --> json文件 --> json.dump(python,f)
with open('demo.json', 'w', encoding='utf-8') as f:
    json.dump(jso, f, ensure_ascii=False)
    
# 读取json文件 --> json.load(f)
with open('demo.json', 'r', encoding='utf-8') as f:
    json.load(f, ensure_ascii=False)
