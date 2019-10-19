with open('demo.js','r') as f:
    js = f.read()
import execjs
w = 'hehe'
sign = execjs.compile(js).call('e',w)
print(sign)















